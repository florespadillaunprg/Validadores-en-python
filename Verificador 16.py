# calcular la dilatacion superficial final que experimenta un cuerpo al cambiar la temperatura
dilatacion_superficial_final,dilatacion_superficial_inicial,beta,temperatura=0.0,0.0,0.0,0.0

# asignacion de valores
dilatacion_superficial_inicial=52
beta=26
temperatura=100

# calculo
dilatacion_superficial_final=dilatacion_superficial_inicial*(1+beta*temperatura)

# verificador
verificador=not(not(dilatacion_superficial_final!=dilatacion_superficial_final))

# mostrar valores
print("dilatacion superficial final =", dilatacion_superficial_final)
print("dilatacion superficial inicial =", dilatacion_superficial_inicial)
print("beta =", beta)
print("temperatura =", temperatura)
print("not(not(dilatacion_superficial_final!=dilatacion_superficial final))=", verificador)
