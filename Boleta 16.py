# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
pintura01=input("Ingrese el color de la pintura01:")
pintura02=input("Ingrese el color de la pintura02:")
pintura03=input("Ingrese el color de la pintura03:")
precio_pintura01=float(input("Ingrese el precio de la pintura01:"))
precio_pintura02=float(input("Ingrese el precio de la pintura02:"))
precio_pintura03=float(input("Ingrese el precio de la pintura03:"))

# PROCESSING
total=(precio_pintura01+precio_pintura02+precio_pintura03)

# VERIFICADOR
total_de_venta=(total!=555)

#OUTPUT
print("#########################")
print("# Ferreteria:     LA VIRGEN DEL CARMEN  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# pintura:", pintura01,"                           precio:  S/.", precio_pintura01)
print("# pintura:", pintura02,"                           precio:  S/.", precio_pintura02)
print("# pintura:", pintura03,"                           precio:  S/.", precio_pintura03)
print("# total:    S/.", total)
print("#########################")
print("# total de venta:", total_de_venta)
