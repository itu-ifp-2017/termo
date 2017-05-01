import matplotlib.pyplot as plt

def thermalExpansionCoefficient(V_1,V_2,V_3,V_4,V_5,V_6,V_7,):
  plt.plot([25,30,40,50.,60,70,80], [V_1,V_2,V_3,V_4,V_5,V_6,V_7])
  plt.xlabel('T2 (°C)')
  plt.ylabel('ΔL (mm))')
  plt.title('The grapf of ΔL with respect to T2')
  a_calculated=np.polyfit(x, y, 1)
  plt.show()
  print "the calculated thermal expansion coefficient of Aluminium is %f." %a_calculated 
  a_real=24
  a_error=abs(a_real-a_calculated)*100.0/a_real
  print "The error percentage of thermal expansion coefficient of Aluminium is %f." %a_error
 
 return a_calculated,a_error
