# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
carro01=input("Ingrese la marca del carro01:")
carro02=input("Ingrese la marca del carro02:")
carro03=input("Ingrese la marca del carro03:")
precio_del_carro01=float(input("Ingrese el precio del carro01:"))
precio_del_carro02=float(input("Ingrese el precio del carro02:"))
precio_del_carro03=float(input("Ingrese el precio del carro03:"))

# PROCESSING
total=(precio_del_carro01+precio_del_carro02+precio_del_carro03)

# VERIFICADOR
ganancia_de_vendedor=(total==100000)

#OUTPUT
print("#########################")
print("# SAC. TOYOTA-PERU")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# carro:", carro01,"                                    precio:  S/.", precio_del_carro01)
print("# carro:", carro02,"                                    precio:  S/.", precio_del_carro02)
print("# carro:", carro03,"                                    precio:  S/.", precio_del_carro03)
print("total:    S/.", total)
print("#########################")
print("# ganancia del vendedor:", ganancia_de_vendedor)
