# calcular la energia de un electron
energia,masa,longitud,tiempo=0.0,0.0,0.0,0.0

# asignacion de valores
masa=5
longitud=10
tiempo=2

# calculo
energia=masa*(longitud**2)/tiempo**2

# verificador
verificador=not(energia<tiempo and masa==longitud)

# mostrar valores
print("energia =", energia)
print("masa =", masa)
print("longitud =", longitud)
print("tiempo =", tiempo)
print("not(energia<tiempo and masa==longitud)=", verificador)
