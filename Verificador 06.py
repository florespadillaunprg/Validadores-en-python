# encontrar el area de un trapecio
area,base_mayor,base_menor,altura=0.0,0.0,0.0,0.0

# asignacion de valores
base_mayor=10
base_menor=6
altura=5

# calculo
area=(base_mayor+base_menor)*altura/2

#verificador
verificador=not(area!=altura or altura>=23)

# mostrar valores
print("area =", area)
print("base mayor =", base_mayor)
print("base menor =", base_menor)
print("altura =", altura)
print("not(area!=altura or altura>=23)=", verificador)
