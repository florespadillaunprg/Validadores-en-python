# calcular el tiempo de encuentro de dos autos
tiempo_de_encuentro,velocida_auto1,velocidad_auto2,distancia=0.0,0.0,0.0,0.0

# asignacion de valores
velocida_auto1=9
velocidad_auto2=6
distancia=150

# calculo
tiempo_de_encuentro=distancia/(velocida_auto1+velocidad_auto2)

#verificador
verificador=not(tiempo_de_encuentro>=distancia)

# mostrar valores
print("tiempo de encuentro =", tiempo_de_encuentro)
print("velocidad auto1 =", velocida_auto1)
print("velocidad auto2 =", velocidad_auto2)
print("distancia =", distancia)
print("not(tiempo_de_encuentro>=distancia)=", verificador)
