# calcular la fuerza centripeta
fuerza_centripeta,masa,velocidad_angular,radio=0.0,0.0,0.0,0.0

# asignacion de valores
masa=6
velocidad_angular=4
radio=15

# calculo
fuerza_centripeta=masa*(velocidad_angular**2)*radio

#verificador
verificador=not(not(fuerza_centripeta<radio or masa!=velocidad_angular))
#mostrar valores
print("fuerza centripeta =", fuerza_centripeta)
print("masa =", masa)
print("velocidad angular =", velocidad_angular)
print("radio", radio)
print("not(not(fuerza_centripeta<radio or masa!=velocidad_angular))=", verificador)
