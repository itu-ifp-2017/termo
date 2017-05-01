import matplotlib.pyplot as plt

def heatcapacity(m_cal,m_ves_cal,T_water,T):
m_water=m_ves_cal-m_cal
c=1.0
T_room=22.0
C=m_water*c*(T_water-T)/(T-T_room)
print "The heat capacity of water is %f cal/°C." %C
return C

def thermalConductivity(ΔT,V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11,V_12,V_13,V_14,V_15,V_16,V_17,V_18,V_19,V_20):
  plt.plot([0,30,60,90.,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570], [V_1,V_2,V_3,V_4,V_5,V_6,V_7,V_8,V_9,V_10,V_11,V_12,V_13,V_14,V_15,V_16,V_17,V_18,V_19,V_20])
  plt.xlabel('t (sn)')
  plt.ylabel('ΔQ (cal))
  plt.title('The grapf of ΔQ with respect to t')
  slope=np.polyfit(x, y, 1)
  plt.show()
   print "ΔQ/Δt is %f." %slope
  Δx=31.5
  A=4.91
  K_calculated=-(slope*Δx)/(A*ΔT)
  K_literature=205.0
  K_error=abs(K_calculated-K_literature)*100.0/K_literature
  print "The percentage error of thermal conductivity of aluminum is %  %f." %K_error
return K_calculated,K_error
