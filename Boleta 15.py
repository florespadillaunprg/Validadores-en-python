# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
avion01=input("Ingrese la marca del avion01:")
avion02=input("Ingrese la marca del avion02:")
avion03=input("Ingrese la marca del avion03:")
precio_de_avion01=float(input("Ingrese el precio del avion01:"))
precio_de_avion02=float(input("Ingrese el precio del avion02:"))
precio_de_avion03=float(input("Ingrese el precio del avion03:"))

# PROCESSING
total=(precio_de_avion01+precio_de_avion02+precio_de_avion03)

# VERIFICADOR
IGV=(total>=21 or 21>=total)

#OUTPUT
print("#########################")
print("# SAC.    AEROLINEA-SIDER-EE.UU")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# avion01:", avion01,"                      precio:  S/.", precio_de_avion01)
print("# avion02:", avion02,"                      precio:  S/.", precio_de_avion02)
print("# avion03:", avion03,"                      precio:  S/.", precio_de_avion03)
print("# total:   S/.", total)
print("#########################")
print("# IGV:", IGV)
