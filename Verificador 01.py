# encotrar el divedendo a partir del algoritmo de la divison
dividendo,divisor,cociente,residuo=0,0,0,0

# asignacion de valores
divisor=10
cociente=5
residuo=2

#calculo
dividendo=(divisor*cociente)+residuo

#verificador
verificador=(dividendo!=52 or divisor==residuo)

# mostrar valores
print("divisor =", divisor)
print("cociente =", cociente)
print("residuo =", residuo)
print("dividendo =", dividendo)
print("(dividendo!=52 or divisor==residuo)=", verificador)
