import tornado
import os
from tornado.options import options, define
import tornado.httpserver
import tornado.ioloop
import tornado.web
import string
import random
from pymongo import MongoClient
import concurrent.futures
import bcrypt
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import uuid
import pandas as pd
import math
from numpy.random import randint
from collections import Counter
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import time

root = os.path.dirname(__file__)
define('port', type=int, default=8080)
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
secret_key = ''.join([random.SystemRandom().choice(chars) for i in range(100)])
settings = {
    "cookie_secret": secret_key,
    "login_url": "/login",
    "template_path": os.path.join(os.path.dirname(__file__), 'views')
}

# A thread pool to be used for password hashing with bcrypt.                                      
executor = concurrent.futures.ThreadPoolExecutor(2)

# Mongo Client
mongoclient = MongoClient('mongodb', 27017)
userdata = mongoclient.userdata
expdata = mongoclient.expdata
autosave = mongoclient.autosave

def serve():
    print "web_server:serve"
    tornado_app = tornado.web.Application([
        ("/", Welcome),
        ("/logout", Logout),
        ("/login", Login),
        ("/register", Register),
        ("/upload", Upload),
        ("/upload/(.*)", Upload),
        ("/deney1", Deney1),
        ("/deney1/(.*)", Deney1),
        ("/deney2", Deney2),
        ("/deney2/(.*)", Deney2),
        ("/deney3", Deney3),
        ("/deney4", Deney4),
        ("/done/(.*)", EmptyTemplateLoader),
        ("/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'plots')})
    ], **settings)
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class TemplateRendering:
    def render_template(self, template_name, variables={}):
        template_dirs = [ settings['template_path'] ]
        env = Environment(loader = FileSystemLoader(template_dirs))

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)

        content = template.render(variables)
        return content

class EmptyTemplateLoader(BaseHandler, TemplateRendering):
    def get(self, pagename=None):
        if pagename == 'users-registered':
            content = self.render_template('register_from_csv_successful.html')
            self.write(content)
    
class Deney1(BaseHandler, TemplateRendering):
    @tornado.web.authenticated
    def get(self, pagename=None):
        if pagename == 'sonuc':
            username = tornado.escape.xhtml_escape(self.current_user)
            query = { 'username': username }
            files = []
            for doc in expdata.binomial_distribution.find(query):
                files.append( int(doc['file'].split('.')[0]) )

            img = str(max(files)) + '.png'
            content = self.render_template('sonuc.html', {'img': '/static/'+str(img)} )
            self.write(content)
            
        else:
            content = self.render_template('binomial_distribution.html')
            self.write(content)

    @tornado.web.authenticated
    def post(self, method):
        username = tornado.escape.xhtml_escape(self.current_user)
        if method == 'data':
            data = []
            for i in self.request.arguments:
                data.append( int(self.request.arguments[i][0]) )
                
            binomial_distribution(data, username)
            self.write('/deney1/sonuc')

        elif method == 'autosave':
            data = self.request.arguments
            document = {'username': username, 'data': data }
            if not autosave.binomial_distribution.find_one({'username':username}):
                cursor = autosave.binomial_distribution.insert_one(document)
            else:
                cursor = autosave.binomial_distribution.update_one({'username':username}, {'$set':document})

def binomial_distribution(data, username):
    numtails = pd.Series(data)
    hdata = pd.Series(Counter(numtails)).reindex(range(0,11)).fillna(0).astype(int)
    plot = hdata.plot(kind='bar')
    fig = plot.get_figure()
    timestamp = int(time.time())
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    document = { 'username': username, 'file': output_file }
    cursor = expdata.binomial_distribution.insert_one(document)

class Deney2(BaseHandler, TemplateRendering):
    def get(self, pagename=None):
        if pagename is None:
            content = self.render_template('heat_capacity_of_solids_part_one.html')
            self.write(content)

        else:
            content = self.render_template('heat_capacity_of_solids_part_two.html')
            self.write(content)

class Deney3(BaseHandler, TemplateRendering):
    def get(self):
        content = self.render_template('fusion_latent_heat_of_water.html')
        self.write(content)


class Deney4(BaseHandler, TemplateRendering):
    def get(self):
        content = self.render_template('thermal_expansion_coefficient_of_solids.html')
        self.write(content)
    
class Welcome(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = tornado.escape.xhtml_escape(self.current_user)
        self.write('<html><body><h2>Hello ' + str(username) + '!</h2></body></html>'
                   '<a href="/logout">Logout</a>')

class Logout(BaseHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect("/")
        
class Login(BaseHandler, TemplateRendering):
    def get(self):
        content = self.render_template('login.html')
        self.write(content)
        # self.write('<html><body><form action="/login" method="post">'
        #            'Username: <input type="text" name="username"> '
        #            'Password: <input type="password" name="password">'
        #            '<input type="submit" value="Sign in">'
        #            '<p>If you do not have an account yet, '
        #            'you can <a href="/register">register here.</a></p>'
        #            '</form></body></html>')

    @tornado.gen.coroutine
    def post(self):
        user_db_hashed_password = get_user_password_from_db(self.get_argument("username"))
        user_input_hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
            tornado.escape.utf8(user_db_hashed_password))
        if user_db_hashed_password == user_input_hashed_password:
            self.set_secure_cookie("username", self.get_argument("username"))
            self.redirect("/")

        else:
            self.write('<html><body><form action="/login" method="post">'
                       'Username: <input type="text" name="username"> '
                       'Password: <input type="password" name="password">'
                       '<input type="submit" value="Sign in"> Wrong password or username!'
                       '<p>If you do not have an account yet, '
                       'you can <a href="/register">register here.</a></p>'
                       '</form></body></html>')
    
class Register(BaseHandler, TemplateRendering):
    def get(self):
        content = self.render_template('register.html')
        self.write(content)
        # self.write('<html><body><form action="/register" method="post">'
        #         'Username: <input type="text" name="username"> '
        #         'Password: <input type="password" name="password">'
        #         '<input type="submit" value="Register">'
        #         '<p>If you already have an account, '
        #         'you can <a href="/login">login here.</a></p>'
        #         '</form></body></html>')

    @tornado.gen.coroutine
    def post(self):
        hashed_password_with_salt = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
            bcrypt.gensalt())
        cursor = register_user(self.get_argument("username"), hashed_password_with_salt)
        if cursor:
            self.set_secure_cookie("username", str( cursor['username'] ))
            self.redirect("/")

        else:
            self.write("user already exists")

class Upload(BaseHandler, TemplateRendering):
    def get(self, error_msg=None):
        variables = {'html':''}
        if error_msg is not None:
            variables['error_msg'] = error_msg
            
        content = self.render_template('upload_csv.html', variables)
        self.write(content)
        
    def post(self, pagename=None):
        if pagename is None:
            if 'filearg' not in self.request.files:
                self.get('No file selected!')

            else:
                fileinfo = self.request.files['filearg'][0]
                separator = ';' if self.get_argument('separator') in ['','1'] else ','
                fname = fileinfo['filename']
                extn = os.path.splitext(fname)[1]
                cname = str(uuid.uuid4()) + extn
                filepath = os.path.join(os.path.dirname(__file__), 'uploads/') + fname 
                fh = open(filepath, 'w')
                fh.write(fileinfo['body'])
                fh.close()
                userlist = pd.read_csv( str(filepath) , sep=separator).dropna(axis='columns', how='all').dropna(axis='rows', how='all')
                userlist.index += 1
                content = self.render_template('upload_csv.html', {
                    'html':userlist.to_html(classes=['ui', 'celled', 'table']),
                    'filename': fname,
                    'columns': userlist.columns,
                    'separator': separator
                })
                self.write(content)
            
        elif pagename == 'register_from_csv':
            fname = self.get_argument('filename')
            id_value = self.get_argument('id_value')
            name_value = self.get_argument('name_value')
            separator = self.get_argument('separator')
            filepath = os.path.join(os.path.dirname(__file__), 'uploads/') + fname 
            register_from_csv( filepath, separator, id_value, name_value )
            self.write({'redirect_url': '/done/users-registered'})

            
def get_user_password_from_db(username):
    query = { 'username': username }
    cursor = userdata.auth.find_one(query)
    if cursor:
        return cursor['password']
    else:
        return None

def register_user(username, hashed_password, student_name=None):
    query = { 'username': username }
    if not userdata.auth.find_one(query):
        document = { 'username': username, 'password': hashed_password }
        if student_name is not None:
            document['student_name'] = student_name
            
        cursor = userdata.auth.insert_one(document)
        return {
            'username': username
        }
    else:
        print "user already exists"
        return None

@tornado.gen.coroutine
def register_from_csv(filepath, separator, id_column, name_column):
    userlist = pd.read_csv( str(filepath) , sep=separator).dropna(axis='columns', how='all').dropna(axis='rows', how='all')
    registered_users = []
    for index, row in userlist.iterrows():
        username = str(row[id_column])
        student_name = str(row[name_column])
        hashed_password_with_salt = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(username),
            bcrypt.gensalt())
        register_user( username, hashed_password_with_salt, student_name )
