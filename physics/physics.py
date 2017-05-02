import pandas as pd
from collections import Counter
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os

def binomial_distribution(data):
    numtails = pd.Series(data)
    hdata = pd.Series(Counter(numtails)).reindex(range(0,11)).fillna(0).astype(int)
    plot = hdata.plot(kind='bar')
    fig = plot.get_figure()
    timestamp = int(time.time())
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))


def heatcapacity(mcup, m1, T1, T2, Teq, m2):
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

def heat_capacity_of_multiple_materials(data, C):
    for key in data:
        heat_cap = calculate_heat_capacity_of_material(data[key], C)
        data[key]['c_material'] = heat_cap['c_material']
        data[key]['rel_error'] = heat_cap['rel_error']

    return data

def calculate_heat_capacity_of_material(material, C):
    c_material = ( ( float(material['Tf']) - float(material['T1']) ) * float(material['m_water']) ) + ( float(C) * ( float(material['Tf']) - float(material['T1']) ) ) / abs ( float(material['m']) * ( float(material['Tf']) - float(material['T1']) ) )
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
        'rel_error': '%'+str(round(L_error,2))
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
def ideal_gas_graph(V_1,V_2,V_3,V_4,V_5,P_1,P_2,P_3,P_4,P_5):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([V_1,V_2,V_3,V_4,V_5], [P_1,P_2,P_3,P_4,P_5],"b")
    ax.set_xlabel('V (cm3)')
    ax.set_ylabel('P (cm-Hg)')
    ax.set_title('The grapf of P with respect to V')
    timestamp = time.time()
    output_file = str(timestamp) + ".png"
    fig.savefig( os.path.join(os.path.dirname(__file__), 'plots/' + output_file))
    return output_file

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
    ax.set_title('The grapf of T with respect to P')
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
def heatcapacity(m_cal,m_ves_cal,T_water,T):
    m_water=m_ves_cal-m_cal
    c=1.0
    T_room=22.0
    C=m_water*c*(T_water-T)/(T-T_room)
    print "The heat capacity of water is %f cal/C." %C
    return C

def thermalConductivity(dT,V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11,V_12,V_13,V_14,V_15,V_16,V_17,V_18,V_19,V_20):
    plt.plot([0,30,60,90.,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570], [V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11,V_12,V_13,V_14,V_15,V_16,V_17,V_18,V_19,V_20])
    plt.xlabel('t (sn)')
    plt.ylabel('dQ (cal)')
    plt.title('The grapf of dQ with respect to t')
    slope=np.polyfit(x, y, 1)
    plt.show()
    print "dQ/dt is %f." %slope
    dx=31.5
    A=4.91
    K_calculated=-(slope*dx)/(A*dT)
    K_literature=205.0
    K_error=abs(K_calculated-K_literature)*100.0/K_literature
    print "The percentage error of thermal conductivity of aluminum is %  %f." %K_error
    return K_calculated,K_error

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
