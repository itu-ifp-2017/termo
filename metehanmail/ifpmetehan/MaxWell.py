from pylab import*
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
V=np.array([1, 2, 3.0,4.1,5.])
F=np.array([1.1,2.,3.4,3.99,4.65])
plotMaxwell(1.,1.,1.,V,F)
