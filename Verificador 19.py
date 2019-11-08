# calcular la fuerza electrica de un electron
fuerza,constante_fisica_electrica,carga1,carga2,distancia=0.0,0.0,0.0,0.0,0.0

# asignacion de valores
constante_fisica_electrica=9000000000
carga1=0.005
carga2=0.002
distancia=500

# calculo
fuerza=(constante_fisica_electrica*carga1*carga2)/(distancia**2)

# verificador
verificador=not(not(not(fuerza<fuerza or distancia!=distancia and carga1==carga2)))

# mostrar valores
print("fuerza =", fuerza)
print("constante fisica electrica =", constante_fisica_electrica)
print("carga1 =", carga1)
print("carga2 =", carga2)
print("distancia =", distancia)
print("not(not(not(fuerza<fuerza or distancia!=distancia and carga1==carga2)))=", verificador)
