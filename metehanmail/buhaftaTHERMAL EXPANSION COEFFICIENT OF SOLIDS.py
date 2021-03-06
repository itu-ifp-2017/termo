﻿import matplotlib.pyplot as plt

def thermalExpansionCoefficient(,V_1,V_2,V_3,V_4,V_5,V_6,V_7,):
  plt.plot([25,30,40,50.,60,70,80], [V_1,V_2,V_3,V_4,V_5,V_6,V_7])
  plt.xlabel('T2 (°C)')
  plt.ylabel('ΔL (mm))
  plt.title('The grapf of ΔL with respect to T2')
  a_calculated=np.polyfit(x, y, 1)
  plt.show()
   print "the calculated thermal expansion coefficient of the material is %f." %a_calculated
   material=raw_input("Choose your material")
 
 if material==Aluminium:
   a_real=24
   a_error=abs(a_real-a_calculated)*100.0/a_real
     print "The error percentage of thermal expansion coefficient of Aluminium is %f." %a_error
  

 elif material==Copper:
   a_real=17
   a_error=abs(a_real-a_calculated)*100.0/a_real
     print "The error percentage of thermal expansion coefficient of Copper is %f." %a_error
     
 elif material==Glass:
   a_real=9
   a_error=abs(a_real-a_calculated)*100.0/a_real
     print "The error percentage of thermal expansion coefficient of Glass is %f." %a_error
     
 elif material==Steel:
   a_real=11
   a_error=abs(a_real-a_calculated)*100.0/a_real
     print "The error percentage of thermal expansion coefficient of Steel is %f." %a_error
     
 elif material==Lead:
   a_real=29
   a_error=abs(a_real-a_calculated)*100.0/a_real
     print "The error percentage of thermal expansion coefficient of Lead is %f." %a_error    
        
 
 else:
  print "invalid material"
 
 return a_calculated
