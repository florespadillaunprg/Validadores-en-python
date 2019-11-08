# encontrar la diagonal principal de un paralelepipedo
diagonal_principal,diagonal01,diagonal02,diagonal03=0,0,0,0

# asignacion de valores
diagonal01=3
diagonal02=4
diagonal03=5

#calculo
diagonal_principal=(diagonal01**2)+(diagonal02**2)+(diagonal03**2)

#verificador
verificador=(diagonal_principal>=23 and diagonal01<diagonal02 or diagonal03==diagonal03)

# mostrar valores
print("diagonal principal =", diagonal_principal)
print("diagonal01 =", diagonal01)
print("diagonal02 =", diagonal02)
print("diagonal03 =", diagonal03)
print("(diagonal principal>=23 and diagonal01<diagonal02 or diagonal03==diagonal03)=", verificador)
