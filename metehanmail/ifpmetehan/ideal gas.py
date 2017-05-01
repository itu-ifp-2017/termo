def graph1(V_1,V_2,V_3,V_4,V_5,P_1,P_2,P_3,P_4,P_5):
  plt.plot([V_1,V_2,V_3,V_4,V_5], [P_1,P_2,P_3,P_4,P_5],"b")
  plt.xlabel('V (cm3)')
  plt.ylabel('P (cm-Hg)')
  plt.title('The grapf of P with respect to V')
  plt.show()
return

def numberOfMol(P,V,T):
  t=T+273.15
  R=8.3145
  n=(P*V)/(R*t)
return n
