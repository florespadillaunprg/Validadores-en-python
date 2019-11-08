# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
pantalon=input("Ingrese la marca de pantalon:")
camisa=input("Ingrese la marca de camisa:")
polo=input("Ingrese la marca de polo:")
precio_del_pantalon=float(input("Ingrese el precio del pantalon:"))
precio_de_la_camisa=float(input("Ingrese el precio de la camisa:"))
precio_del_polo=float(input("Ingrese el precio del polo:"))

# PROCESSING
total=(precio_del_pantalon+precio_de_la_camisa+precio_del_polo)

# VERIFICADOR
ganancia_obtenida=(total<1)

#OUTPUT
print("#########################")
print("# Centro comercial:    EL ELEGANTE  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# pantalon:", pantalon,"                           precio:   S/.", precio_del_pantalon)
print("# camisa:", camisa,"                               precio:   S/.", precio_de_la_camisa)
print("# polo:", polo,"                                   precio:   S/.", precio_del_polo)
print("# total:   S/.", total)
print("#########################")
print("# ganancia obtenida:", ganancia_obtenida)
