# INPUT
cliente=input("Ingrese el nombre del cliente:")
DNI=int(input("Ingrese el numero de DNI:"))
platos=int(input("Ingrese la cantidad de platos:"))
cucharas=int(input("Ingrese la cantidad de cucharas:"))
ollas=int(input("Ingrese la cantidad de ollas:"))
precio_de_un_plato=float(input("Ingrese el precio de un plato:"))
precio_de_una_cuchara=float(input("Ingrese el precio de una cuchara:"))
precio_de_una_olla=float(input("Ingrese el precio de una olla:"))

# PROCESSING
total=((platos*precio_de_un_plato)+(cucharas*precio_de_una_cuchara)+(ollas*precio_de_una_olla))

# VERIFICADOR
impuesto=not(total>=precio_de_una_olla and total!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:      EL PIURANITO ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# platos:", platos,"                    precio:  S/.", precio_de_un_plato)
print("# cucharas:", cucharas,"                precio:  S/.", precio_de_una_cuchara)
print("# ollas:", ollas,"                      precio:  S/.", precio_de_una_olla)
print("# total:    S/.", total)
print("#########################")
print("# impuesto:", impuesto)
