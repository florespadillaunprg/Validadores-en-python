# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
lapiceros=int(input("Ingrese la cantidad de lapiceros:"))
lapices=int(input("Ingrese la cantidad de lapices:"))
borradores=int(input("Ingrese la cantidad de borradores:"))
precio_de_lapicero=float(input("Ingrese el precio de un lapicero:"))
precio_de_un_lapiz=float(input("Ingrese el precio de un lapiz:"))
precio_de_un_borrador=float(input("Ingrese el precio de un borrador:"))

#PROCESSING
total=((lapiceros*precio_de_lapicero)+(lapices*precio_de_un_lapiz)+(borradores*precio_de_un_borrador))

# VERIFICADOR
precio_de_compra=not(total!=65)

#OUTPUT
print("#########################")
print("# Libreria:     CAYETANO HEREDIA")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# lapiceros:", lapiceros,"                       precio:  S/.", precio_de_lapicero)
print("# lapices:", lapices,"                           precio:  S/.", precio_de_un_lapiz)
print("# borradores:", borradores,"                     precio:  S/.", precio_de_un_borrador)
print("# total:   S/.", total)
print("#########################")
print("# precio de compra:", precio_de_compra)
