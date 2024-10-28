# import m_factorial2 as mf

# fact5 = mf.factorial(5)
# print(f'El factorial de 5 es: {fact5}')

# Aquí imprime m_factorial2 porque se esta ejecutando desde un ambito superior app3.py y posterior realiza la
# función programada

import sys
print(sys.path)

sys.path.append("xxxxxxxxxx")
print(sys.path)

import m_factorial2
print(dir(m_factorial2))

print(dir(sys))