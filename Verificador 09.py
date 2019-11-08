# calcular la presion que ejerce un cuerpo sobre otro
presion,masa,longitud,tiempo=0.0,0.0,0.0,0.0

# asignacion de valores
masa=100000
longitud=10
tiempo=10

# calculo
presion=masa/(longitud*(tiempo**2))

#verificador
verificador=(presion!=presion or presion>=presion)

# mostrar valores
print("presion =", presion)
print("masa =", masa)
print("longitud =", longitud)
print("tiempo =", tiempo)
print("(presion!=presion or presion>=presion)=", verificador)
