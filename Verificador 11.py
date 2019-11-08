# calcular el tiempo de alcance que realiza un auto para alcanzar un camion
tiempo_de_alcance,velocidad_del_auto,velocidad_del_camion,distancia_recorrida=0.0,0.0,0.0,0.0

# asignacion de valores
velocidad_del_auto=10
velocidad_del_camion=5
distancia_recorrida=100

# calculo
tiempo_de_alcance=distancia_recorrida/(velocidad_del_auto-velocidad_del_camion)

#verificador
verificador=not(not(not(tiempo_de_alcance!=54 or distancia_recorrida<velocidad_del_auto)))

# mostrar valores
print("tiempo de alcance =", tiempo_de_alcance)
print("velocidad del auto =", velocidad_del_auto)
print("velocidad del camion =", velocidad_del_camion)
print("distancia recorrida =", distancia_recorrida)
print("not(not(not(tiempo_de_alcance!=54 or distancia_recorrida<velocidad_del_auto)))=", verificador)
