# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
colonia=input("Ingrese la marca de la colonia:")
desodorante=input("Ingrese la marca del desodorante:")
talco=input("Ingrese la marca del talco:")
precio_de_la_colonia=float(input("Ingrese el precio de la colonia:"))
precio_del_desodorante=float(input("Ingrese el precio del desodorante:"))
precio_del_talco=float(input("Ingrese el precio del talco:"))

# PROCESSING
total=(precio_de_la_colonia+precio_del_desodorante+precio_del_talco)

# VERIFICADOR
numero_de_venta=(total!=23 or 23==total)

#OUTPUT
print("#########################")
print("# Perfumeria:       FLORES    ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# colonia:", colonia,"                                     precio:   S/.", precio_de_la_colonia)
print("# desodorante:", desodorante,"                             precio:    S/.", precio_del_desodorante)
print("# talco:", talco,"                                         precio:    S/.", precio_del_talco)
print("# total:    S/.", total)
print("#########################")
print("# numero de venta:", numero_de_venta)
