#INPUT
cliente=input("Ingrese nombre y apellidos:")
numero_de_DNI=int(input("Ingrese numero de DNI:"))
numero_de_RUC=int(input("Ingrese numero de RUC:"))
marca_de_cuaderno01=input("Ingrese marca de cuaderno01:")
marca_de_cuaderno02=input("Ingrese marca de cuaderno02:")
marca_de_cuaderno03=input("Ingrese marca de cuaderno03:")
precio_de_cuaderno01=float(input("Ingrese precio de cuaderno01:"))
precio_de_cuaderno02=float(input("Ingrese precio de cuaderno02:"))
precio_de_cuaderno03=float(input("Ingrese precio de cuaderno03:"))

#PROCESSING
total_a_pagar=(precio_de_cuaderno01+precio_de_cuaderno02+precio_de_cuaderno03)

#vVERIFICADOR
total_a_gastar=(not(total_a_pagar<655))

#OUTPUT
print("###########################")
print("#  Librería:     ILUSIONES DEL SABER")
print("###########################")
print("# cliente:", cliente)
print("# DNI:", numero_de_DNI)
print("# RUC:", numero_de_RUC)
print("# cuaderno01:", marca_de_cuaderno01,"            # precio:  S/.", precio_de_cuaderno01)
print("# cuaderno02:", marca_de_cuaderno02,"            # precio:  S/.", precio_de_cuaderno02)
print("# cuaderno03:", marca_de_cuaderno03,"            #  precio:  S/.", precio_de_cuaderno03)
print("# total:  S/.", total_a_pagar)
print("###########################")
print("# total a gastar:", total_a_gastar)
