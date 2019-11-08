# INPUT
cliente=input("Ingrese el nombre del cliente:")
numero_de_RUC=int(input("Ingrese el numero de RUC:"))
televisor=input("Ingrese la marca de televisor:")
licuadora=input("Ingrese la marca de la licuadora:")
refrigeradora=input("Ingrese la marca de la refrigeradora:")
precio_del_televisor=float(input("Ingrese el precio del televisor:"))
precio_de_la_licuadora=float(input("Ingrese el precio de la licuadora:"))
precio_de_la_refrigeradora=float(input("Ingrese el precio de la refrigeradora:"))

# PROCESSING
total=(precio_del_televisor+precio_de_la_licuadora+precio_de_la_refrigeradora)

# VERIFICADOR
precio_de_venta=(total==total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA CHICLAYANITA")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", numero_de_RUC)
print("# televisor:", televisor,"                       precio:  S/.", precio_del_televisor)
print("# licuadora:", licuadora,"                       precio:  S/.", precio_de_la_licuadora)
print("# refrigeradora:", refrigeradora,"               precio:  S/.", precio_de_la_refrigeradora)
print("# total:   S/.", total)
print("#########################")
print("# precio de venta:", precio_de_venta)
