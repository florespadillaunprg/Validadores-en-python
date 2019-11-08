# calcular la distancia que recorre una persona desde chiclayo a lambayeque
distancia,velocidad_inicial,aceleracion,tiempo=0.0,0.0,0.0,0.0

# asignacion de valores
velocidad_inicial=70
aceleracion=7
tiempo=2

# calculo
distancia=(velocidad_inicial*tiempo)+(aceleracion*(tiempo**2)/2)

#verificador
verificador=(distancia<=aceleracion or tiempo>=velocidad_inicial)

# mostrar valores
print("distancia =", distancia)
print("velocidad inicial =", velocidad_inicial)
print("aceleracion =", aceleracion)
print("tiempo =", tiempo)
print("(distancia<=aceleracion or tiempo>=velocidad_inicial)=", verificador)
