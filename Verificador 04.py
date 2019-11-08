# encontrar el area total de un tranco de cono de revolucion
area_total,area_lateral,pi,radio_mayor,radio_menor=0.0,0.0,0.0,0.0,0.0

# asignacion de valores
area_lateral=100
pi=3.14
radio_mayor=10
radio_menor=8

# calculo
area_total=area_lateral+pi*(radio_mayor**2)+pi*(radio_menor**2)

#verificador
verificador=not(area_total<10 or 65>area_lateral)

# mostrar valores
print("area total =", area_total)
print("area lateral =", area_lateral)
print("pi =", pi)
print("radio mayor =", radio_mayor)
print("radio menor =", radio_menor)
print("not(area_total<10 or 65>area_lateral)=", verificador)
