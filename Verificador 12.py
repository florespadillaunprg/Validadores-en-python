# calcular la velocidad final de una particula al frenar bruscamente
velocidad_final,velocidad_inicial,aceleracion,tiempo=0.0,0.0,0.0,0.0

# asignacion de valores
velocidad_inicial=80
aceleracion=8
tiempo=3

# calculo
velocidad_final=velocidad_inicial-(aceleracion*tiempo)

#verificador
verificador=not(velocidad_final>=1000 and aceleracion!=tiempo)

# mostrar valores
print("velocidad final =", velocidad_final)
print("velocidad inicial =", velocidad_inicial)
print("aceleracion =", aceleracion)
print("tiempo =", tiempo)
print("not(velocidad_final>=1000 and aceleracion!=tiempo)=", verificador)
