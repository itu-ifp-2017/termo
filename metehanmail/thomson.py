import matplotlib.pyplot as plt

def jouleThomson(T,V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11):
  gas=raw_input("Choose your gas")
  plt.plot([100,90,80,70.,60,50,40,30,20,10,0], [V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11])
  plt.xlabel('P (kPa))')
  plt.ylabel('ΔT (K)')
  plt.title('The grapf of ΔT with respect to P')
  slope=np.polyfit(x, y, 1)
  plt.show()
  mu_calculated=slope*0.01
   print "the calculated Joule-Thomson coefficient is %f." %mu_calculated
 if gas==CO2:
   a=3.60
   b=42.70
   cp=366.10
   R=8.3145
   mu_real=((2.0*a)/(R*T)-b)*(1.0/cp)
   mu_error=abs(mu_real-mu_calculated)*100.0/mu_real
     print "The error percentage of the Joule-Thomson coefficient for Carbon dioxide is %f." %mu_error
  

 elif gas==N2:
   a=1.40
   b=39.10
   cp=288.90
   R=8.3145
   mu_real=((2.0*a)/(R*T)-b)*(1.0/cp)
   mu_error=abs(mu_real-mu_calculated)*100.0/mu_real
     print "The error percentage of the Joule-Thomson coefficient for Nitrogen is %f." %mu_error
  
 
 else:
  print "invalid gas"
 
 return mu_calculated
