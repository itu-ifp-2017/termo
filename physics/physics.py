import pandas as pd
from collections import Counter
import time

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

def dene(glass,iron,graphite,C):
    c_real = {
        'copper': 0.0923,
        'aluminium': 0.215,
        'porcelain': 0.26
    }

def calculate_heat_capacity_of_material(material, C):
    c_material = ( ( material['Tf'] - material['T1'] ) * material['m_water'] ) + ( C * ( material['Tf'] - material['T1'] ) ) / abs ( material['m'] * ( material['Tf'] - material['T1'] ) )
    rel_error = abs( material['c_real'] - c_material ) * 100.0 / material['c_real']
