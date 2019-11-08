# encontrar el valor de la fuerza realizado por una particula
fuerza,masa,longitud,tiempo=0.0,0.0,0.0,0.0

# asignacion de valores
masa=10
longitud=20
tiempo=2

# calculo
fuerza=(masa*longitud)/tiempo**2

# verificador
verificador=(fuerza==tiempo or masa!=longitud)

# mostrar valores
print("fuerza =", fuerza)
print("masa =", masa)
print("longitud =", longitud)
print("tiempo =", tiempo)
print("(fuerza==tiempo or masa!=longitud)=", verificador)
