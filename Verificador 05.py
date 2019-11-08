# encontrar el volumen de un tronco de cono de revolucion
volumen,pi,altura,radio_menor,radio_mayor=0.0,0.0,0.0,0.0,0.0

# asignacion de valores
pi=3.14
altura=20
radio_menor=8
radio_mayor=10

# calculo
volumen=pi*altura*(radio_menor**2+radio_mayor**2+radio_menor*radio_mayor)/3

#verificador
verificador=(volumen==radio_mayor and altura<=pi)

# mostrar valores
print("volumen =", volumen)
print("pi =", pi)
print("altura =", altura)
print("radio menor =", radio_menor)
print("radio mayor =", radio_mayor)
print("(volumen==radio_mayor or altura<=pi)=", verificador)
