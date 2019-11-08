# INPUT
cliente=input("Ingrese el nombre del cliente:")
numero_de_DNI=int(input("Ingrese el numero de DNI:"))
numero_de_RUC=int(input("Ingrese el numero de RUC:"))
marca_de_celular01=input("Ingrese la marca del celular01:")
marca_de_celular02=input("Ingrese la marca del celular02:")
marca_de_celular03=input("Ingrese la amrca del celular03:")
precio_del_celular01=float(input("Ingrese el precio del celular01:"))
precio_del_celular02=float(input("Ingrese el precio del celular02:"))
precio_del_celular03=float(input("Ingrese el precio del celular03:"))

# PROCESSING
total=(precio_del_celular01+precio_del_celular02+precio_del_celular03)

# VERIFICADOR
ganacia=(total==total and total!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA NUEVA TECNOLOGIA ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", numero_de_DNI)
print("# RUC:", numero_de_RUC)
print("# celular:", marca_de_celular01,"               precio:  S/.", precio_del_celular01)
print("# celular:", marca_de_celular02,"               precio:  S/.", precio_del_celular02)
print("# celular:", marca_de_celular03,"               precio:  S/.", precio_del_celular03)
print("# total:  S/.", total)
print("#########################")
print("# ganancia:", ganacia)
