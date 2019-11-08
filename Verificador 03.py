# encontrar el area lateral de un tronco de revolucion
area_lateral,pi,radio_mayor,radio_menor,generatriz=0.0,0.0,0.0,0.0,0.0

#  asignacion de valores
pi=3.14
radio_mayor=8
radio_menor=4
generatriz=10

# calculo
area_lateral=pi*(radio_mayor+radio_menor)*generatriz

#verificador
verificador=not(area_lateral!=53 and 23>=area_lateral)

# mostrar valores
print("area lateral =", area_lateral)
print("pi =", pi)
print("radio mayor =", radio_mayor)
print("radio menor =", radio_menor)
print("generatriz =", generatriz)
print("not(area_lateral!=53 and 23>=area_lateral)=", verificador)
