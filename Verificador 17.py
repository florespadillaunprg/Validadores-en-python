# calcular el calor especifico de un cuerpo
calor_especifico,cantidad_de_calor,masa,variacion_de_temperatura=0.0,0.0,0.0,0.0

# asignacion de valores
cantidad_de_calor=16
masa=2
variacion_de_temperatura=50

# calculo
calor_especifico=cantidad_de_calor/(masa*variacion_de_temperatura)

#verificador
verificador=not(not(not(calor_especifico<masa or masa!=2)))

# mostrar valores
print("calor especifico =", calor_especifico)
print("cantidad de calor=", cantidad_de_calor)
print("masa =", masa)
print("variacion de temperatura =", variacion_de_temperatura)
print("not(not(not(calor_especifico<masa or masa!=2)))=", verificador)
