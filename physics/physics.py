import pandas as pd
from collections import Counter
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os

def binomial_distribution(data):
    numtails = pd.Series(data)
    hdata = pd.Series(Counter(numtails)).fillna(0) # .reindex(range(0,11)).fillna(0).astype(int)
    plot = hdata.plot(kind='bar')
    fig = plot.get_figure()
    timestamp = int(time.time())
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    return output_file


def heat_capacity_of_solids(mcup, m1, T1, T2, Teq, m2):
    m = m1 - mcup
    M = m2 - m1
    c = 1.0
    delta_m = 2 * 0.05
    delta_T = 1
    C = ( M * c * ( T2 - Teq ) - m * c * ( Teq - T1 ) ) / ( Teq - T1 )
    p_1 = ( c * ( T2 - Teq ) + c * ( Teq - T1 ) ) * delta_m / ( Teq - T1 )
    p_2 = C
    p_3 = abs( ( T2 - Teq ) - ( Teq - T1) ) * 2 * M * c / (( Teq - T1 ) * ( Teq - T1 ))
    delta_C = p_1 + p_2 + p_3
    r_error = delta_C / C
    return {
        'M': round(M,2),
        'ccal': round(C,2),
        'abs_error': round(delta_C,2),
        'rel_error': '%'+str(round(r_error,2))
    }

def heat_capacity_of_multiple_materials(data, m, C):
    for key in data:
        heat_cap = calculate_heat_capacity_of_material(data[key], m, C)
        data[key]['c_material'] = heat_cap['c_material']
        data[key]['rel_error'] = heat_cap['rel_error']

    return data

def calculate_heat_capacity_of_material(material, m, C):
    c_material = ( ( float(material['Tf']) - float(material['T1']) ) * float(material['m_water']) ) + ( float(C) * ( float(material['Tf']) - float(material['T1']) ) ) / abs ( m * ( float(material['Tf']) - float(material['T1']) ) )
    rel_error = abs( float(material['c_real']) - c_material ) * 100.0 / float(material['c_real'])
    return {
        'c_material': round(c_material, 2),
        'rel_error': '%'+str(round(rel_error, 2))
    }

def latent_heat_of_water(m1, m2, T1, m3, T2):
    m1 = float(m1)
    m2 = float(m2)
    m3 = float(m3)
    T1 = float(T1)
    T2 = float(T2)
    m_water = m2 - m1
    m_ice = m3 - m2
    c_water = 1.0
    m_1c_c = 30.0
    Q_out = m_1c_c * ( T1 - T2 ) + m_water * c_water * ( T1 - T2 )
    # print "The heat (Qout) energy given off by the vessel+hot water equals to %f" %Q_out
    L = ( m_1c_c * ( T1 - T2 ) + m_water * c_water * ( T1 - T2 ) - m_ice * c_water * T2 ) / m_ice
    # print "The Latent heat for solid to liquid phase change of water is %f" %L
    L_literature = 80.0
    L_error = abs( L - L_literature ) * 100.0 / L_literature
    # print "The error percentage of L is  %  %f." %L_error
    return {
        'Q_out': round(Q_out, 2),
        'L': round(L, 2),
        'rel_error': '%'+str(round(L_error,2)),
        'm_water': round(m_water,2),
        'm_ice': round(m_ice,2)
    }

def thermal_expansion_coefficient(T1, L1, L2, L3, L4, L5, L6, L7, L8, a_real=24):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [T1,25,30,40,50.,60,70,80]
    y = [0, L2, L3, L4, L5, L6, L7, L8]
    ax.plot(x, y)
    ax.set_xlabel('T2 (C)')
    ax.set_ylabel('L (mm))')
    ax.set_title('The grapf of L with respect to T2')
    timestamp = int(time.time())
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    slope, b = np.polyfit(x, y, 1) # y = slope*x+b
    a = 0 # formul foyde
    a_error=abs(a_real-a)*100.0/a_real
    return {
        'a': a,
        'rel_error': '%'+str(round(a_error,2)),
        'fig': output_file,
        'slope': slope
    }

# ideal gas law
def ideal_gas_plots(data):
    f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, sharex=True, sharey=True)
    ax1.plot( ideal_sub( **data['10'] )['x'], ideal_sub( **data['10'] )['y'], label="10 C" )
    ax1.set_title('The graph of P with respect to V')
    ax2.plot( ideal_sub( **data['20'])['x'], ideal_sub( **data['20'] )['y'], label="20 C" )
    ax3.plot( ideal_sub( **data['30'])['x'], ideal_sub( **data['30'] )['y'], label="30 C" )
    ax3.set_ylabel('P (cm-Hg)')
    ax4.plot( ideal_sub( **data['40'])['x'], ideal_sub( **data['40'] )['y'], label="40 C" )
    ax5.plot( ideal_sub( **data['50'])['x'], ideal_sub( **data['50'] )['y'], label="50 C" )
    ax6.plot( ideal_sub( **data['60'])['x'], ideal_sub( **data['60'] )['y'], label="60 C" )
    ax6.set_xlabel('V (cm3)')
    ax1.legend(loc='upper right', shadow=True)
    ax2.legend(loc='upper right', shadow=True)
    ax3.legend(loc='upper right', shadow=True)
    ax4.legend(loc='upper right', shadow=True)
    ax5.legend(loc='upper right', shadow=True)
    ax6.legend(loc='upper right', shadow=True)
    # Fine-tune figure; make subplots close to each other and hide x ticks for
    # all but bottom plot.
    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    timestamp = time.time()
    output_file = str(timestamp) + ".png"
    plt.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    return output_file
        

def ideal_sub(V_1,V_2,V_3,V_4,V_5,P_1,P_2,P_3,P_4,P_5):
    return {
        'x': [V_1,V_2,V_3,V_4,V_5],
        'y': [P_1,P_2,P_3,P_4,P_5]
        }

def numberOfMol(P,V,T):
    t=T+273.15
    R=8.3145
    n=(P*V)/(R*t)
    return n

# joule thomson
def joule_thomson(V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11, gas):
    x = [100,90,80,70.,60,50,40,30,20,10,0]
    y = [V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlabel('P (kPa))')
    ax.set_ylabel('T (K)')
    ax.set_title('The graph of T with respect to P for ' + gas)
    timestamp = time.time()
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    mu , b = np.polyfit(x, y, 1)
    mu_real=7.16*(10**-6) if gas == 'CO2' else 3.75*(10**-6)
    mu_error=abs(mu_real-mu)*100.0/mu_real
    return {
        'mu': round(mu,2),
        'rel_error': '%'+str(round(mu_error,2)),
        'fig': output_file
    }
    
# thermal conductivity
def thermal_conductivity_part_one(mcal,mw_mcup,twater,teq):
    m_water=mw_mcup-mcal
    c=1.0
    T_room=22.0
    ccal=m_water*c*(twater-teq)/(teq-T_room)
    return {
        'mhot': round(m_water,2),
        'ccal': round(ccal,2)
    }

def thermal_conductivity_part_two(data):
    dq = [0]
    dt = [] # for average dt
    for i in range(9):
        dt.append( data['dt_'+str(i+1)] )
        dq.append(
            (data['dt_'+str(i+2)] - data['dt_1']) * (data['mcold'] + data['ccal'])
        )
        
    t = [0,180,360,540,720,900,1080,1260,1440,1620]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(t, dq)
    ax.set_xlabel('t (sn)')
    ax.set_ylabel('dQ (cal)')
    ax.set_title('The graph of dQ with respect to t')
    slope , b = np.polyfit(t, dq, 1)
    dx=31.5
    A=4.91
    K_calculated=6*(-(slope*dx)/(A*np.mean(dt)))
    K_literature=0.5 # (cal/sec)/(cm2 C/cm)
    K_error=abs(K_calculated-K_literature)*100.0/K_literature
    timestamp = time.time()
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    return {
        'K_calculated': round(K_calculated,2),
        'K_error': '%'+str(round(K_error,2)),
        'fig': output_file,
        'slope': round(slope,2)
    }


# maxwellian
from pylab import *
import math
import numpy as np

def plotMaxwell(M,R,T,Vin,Fin):
    Vmin=V.min()
    Vmax=V.max()
    Vout=np.linspace(Vmin,Vmax,100);
    fout=4*pi(M/(2*pi*R*T))**(3/2)*math.exp(-M*Vout/(2*R*T));
    fig=figure()
    ax=fig.gca()
    ax.set_xlabel("V")
    ax.set_ylabel("F(V)")
    ax.plot(Vout,fout)
    ax.plot(Vin,Fin,'x')
    #return V1D,f

#example for function call
# V=np.array([1, 2, 3.0,4.1,5.])
# F=np.array([1.1,2.,3.4,3.99,4.65])
# plotMaxwell(1.,1.,1.,V,F)
