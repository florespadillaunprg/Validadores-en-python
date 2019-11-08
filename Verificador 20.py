# calcular la resistencia electrica de un condensador
resistencia_electrica,longitud_del_conductor,area_de_la_seccion_recta,resistividad_electrica=0.0,0.0,0.0,0.0

# asignacion de valores
longitud_del_conductor=15
area_de_la_seccion_recta=20
resistividad_electrica=30

# calculo
resistencia_electrica=(resistividad_electrica*longitud_del_conductor)/area_de_la_seccion_recta

# verificador
verificador=not(resistencia_electrica==resistencia_electrica or area_de_la_seccion_recta>=1)

# mostrar valores
print("resistencia electrica =", resistencia_electrica)
print("longitud del conductor =", longitud_del_conductor)
print("area de la seccion recta =", area_de_la_seccion_recta)
print("resistividad electrica =", resistividad_electrica)
print("not(resistencia_electrica==resistencia_electrica or area_de_la_seccion_recta>=1)=", verificador)
