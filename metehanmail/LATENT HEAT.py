def latent_heat_of_water(m_1,m_2,T_1,m_3,T_2):
  m_water=m_2-m_1
  m_ice=m_3-m_2
  c_water=1.0
  m_1c_c=30.0
  Q_out=m_1c_c*(T_1-T_2)+m_water*c_water*(T_1-T_2)
  print "The heat (Qout) energy given off by the vessel+hot water equals to %f" %Q_out
  L=(m_1c_c*(T_1-T_2)+m_water*c_water*(T_1-T_2)-m_ice*c_water*T_2)/m_ice
  print "The Latent heat for solid to liquid phase change of water is %f" %L
  L_literature=80.0
  L_error=abs(L_calculated-L_literature)*100.0/L_literature
  print "The error percentage of L is  %  %f." %L_error
return L
