# calcular la presion que ejerce un cuerpo en un estado termodinamico
presion,volumen,masa,cantidad_de_sustancia,temperatura_absoluta,constante_universal_de_los_gases=0.0,0.0,0.0,0.0,0.0,0.0

# asignacion de valores
volumen=200
masa=5
cantidad_de_sustancia=10
temperatura_absoluta=100
constante_universal_de_los_gases=8.31

# calculo
presion=(cantidad_de_sustancia*constante_universal_de_los_gases*temperatura_absoluta)/volumen

# verificador
verificador=(presion==volumen and masa==presion)

# mostrar valores
print("presion =", presion)
print("volumen =", volumen)
print("masa =", masa)
print("cantidad de sustancia =", cantidad_de_sustancia)
print("temperatura absoluta =", temperatura_absoluta)
print("constante universal de los gases =", constante_universal_de_los_gases)
print("(presion==volumen and masa==presion)=", verificador)
