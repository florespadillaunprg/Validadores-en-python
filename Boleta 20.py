# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
relojes=int(input("Ingrese la cantidad de relojes:"))
pulseras=int(input("Ingrese la cantidad de pulseras:"))
cadenas=int(input("Ingrese la cantidad de cadenas:"))
precio_de_un_reloj=float(input("Ingrese el precio de un reloj:"))
precio_de_una_pulsera=float(input("Ingrese el precio de una pulsera:"))
precio_de_una_cadena=float(input("Ingrese el precio de una cadena:"))

# PROCESSING
total=((relojes*precio_de_un_reloj)+(pulseras*precio_de_una_pulsera)+(cadenas*precio_de_una_cadena))

# VERIFICADOR
precio_de_venta=not(total<=pulseras and relojes!=cadenas)

#OUTPUT
print("#########################")
print("# Joyeria:       EL MILLONARIO   ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# relojes:", relojes,"                                   precio:  S/.", precio_de_un_reloj)
print("# pulseras:", pulseras,"                                 precio:  S/.", precio_de_una_pulsera)
print("# cadenas:", cadenas,"                                   precio:  S/.", precio_de_una_cadena)
print("# total:   S/.", total)
print("#########################")
print("# precio de venta:", precio_de_venta)
