# calcular el empuje hidrostatico de un cuerpo sumergido en un liquido
empuje,densidad_liquido,gravedad,volumen_sumergido=0.0,0.0,0.0,0.0

# asignacion de valores
densidad_liquido=37.3
gravedad=9.8
volumen_sumergido=8

# calculo
empuje=(densidad_liquido*gravedad*volumen_sumergido)

# verificador
verificador=(empuje==empuje and gravedad!=gravedad)

# mostrar valores
print("empuje =", empuje)
print("dendidad del liquido =", densidad_liquido)
print("gravedad =", gravedad)
print("volumen sumergido", volumen_sumergido)
print("(empuje==empuje and gravedad!=gravedad)=", verificador)
