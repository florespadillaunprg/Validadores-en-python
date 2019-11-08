# INPUT
cliente=input("Ingrese el nombre del cliente:")
DNI=int(input("Ingrese el numero d DNI:"))
RUC=int(input("Ingrese el numero de RUC:"))
zapatillas=input("Ingrese marca de zapatillas:")
zapatos=input("Ingrese marca de zapatos:")
chimpunes=input("Ingrese marca de chimpunes:")
precio_de_zapatillas=float(input("Ingrese el precio de las zapatillas:"))
precio_de_zapatos=float(input("Ingrese el precio de los zapatos:"))
precio_de_chimpunes=float(input("Ingrese elprecio de los chimpunes:"))

# PROCESSING
total=(precio_de_zapatillas+precio_de_zapatos+precio_de_chimpunes)

# VERIFICADOR
perdida=(total!=65)

#OUTPUT
print("#########################")
print("# Centro de calzado:     EL AMANECER  ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# RUC:", RUC)
print("# zapatillas:", zapatillas,"                        precio:  S/.", precio_de_zapatillas)
print("# zapatos:", zapatos,"                              precio:  S/.", precio_de_zapatos)
print("# chimpunes:", chimpunes,"                          precio:  S/.", precio_de_chimpunes)
print("# total:    S/.", total)
print("#########################")
print("# perdida:", perdida)
