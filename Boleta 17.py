# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
tubos=int(input("Ingrese cantidad de tubos:"))
fierros=int(input("Ingrese la cantidad de fierros:"))
clavos=int(input("Ingrese la cantidad de clavos:"))
precio_de_un_tubo=float(input("Ingrese el precio de un tubo:"))
precio_de_un_fierro=float(input("Ingrese el precio de un fierro:"))
precio_de_un_clavo=float(input("Ingrese el precio de un clavo:"))

# PROCESSING
total=((tubos*precio_de_un_tubo)+(fierros*precio_de_un_fierro)+(clavos*precio_de_un_clavo))

# VERIFICADOR
impuesto=(total<total)

#OUTPUT
print("#########################")
print("# Ferreteria:       EL LAMBAYECANO   ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# tubos:", tubos,"                      precio:  S/.", precio_de_un_tubo)
print("# fierros:", fierros,"                  precio:   S/.", precio_de_un_fierro)
print("# clavos:", clavos,"                    precio:   S/.", precio_de_un_clavo)
print("# total:   S/.", total)
print("#########################")
print("# impuesto:", impuesto)
