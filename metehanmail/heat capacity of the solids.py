def heatcapacity(m_cup,m_1,T_1,T_2,T_eq,m_2,M):
m=m_1-m_cup
c=1.0
C=((M*c*(T_2-T_eq)-m*c*(T_eq-T_1))/(T_eq-T_1)
print "The heat capacity of the calorimeter vessel is %f cal/°C." %C
p_1=(c*(T_2-T_eq)+c(T_eq-T_1))*delta_m/(T_eq-T_1)
P_2=(M*(T_2-T_eq)+m*(T_eq-T_1))*delta_c/(T_eq-T_1)
p_3=abs(T_2-T_eq)*delta_T*2*M*C/(T_eq-T_1)**2
delta_C=p_1+p_2+p_2+p_3
delta_C=p_1+p_2+p_2+p_3
print "The absolute error of ΔC is %f." %delta_C
r_error=delta_C/C
print "The relative error of (ΔC/C) is %f." %r_error
return C

def cupper(m_water,T_2,m,T_1,T_f):
material=raw_input("Choose your material")

if material==copper:
c_material=((T_f-T_1)*m_water*c)+(C*(T_f-T_1))/abs(m_*(T_f-T_1))
print "The specific heat capacity of Copper %f cal/g°C." % c_material
c_real=0.0923
c_error=abs(c_real-c_material)*100.0/c_real
print "The error percentage of Copper is  %  %f." %c_error

elif material==aluminium:
c_material=((T_f-T_1)*m_water*c)+(C*(T_f-T_1))/abs(m_*(T_f-T_1))
print "The specific heat capacity of Aluminium %f cal/g°C." % c_material
c_real=0.215
c_error=abs(c_real-c_material)*100.0/c_real
print "The error percentage of Aluminium is  %  %f." %c_error

elif material==porcelain:
c_material=((T_f-T_1)*m_water*c)+(C*(T_f-T_1))/abs(m_*(T_f-T_1))
print "The specific heat capacity of Porcelain %f cal/g°C." %c_material
c_real=0.26
c_error=abs(c_real-c_material)*100.0/c_real
print "The error percentage of Porcelain is  %  %f." %c_error

else:
  print "invalid material"

return c_material
