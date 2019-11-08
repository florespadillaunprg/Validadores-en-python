# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
mesas=int(input("Ingrese la cantidad de mesas:"))
sillas=int(input("Ingrese la cantidad de sillas:"))
carpetas=int(input("Ingrese la cantidad de carpetas:"))
precio_de_una_mesa=float(input("Ingrese el precio de una mesa:"))
precio_de_una_silla=float(input("Ingrese el precio de una silla:"))
precio_de_una_carpeta=float(input("Ingrese el precio de una carpeta:"))

# PROCESSING
total=((mesas*precio_de_una_mesa)+(sillas*precio_de_una_silla)+(carpetas*precio_de_una_carpeta))

# VERIFICADOR
precio_de_venta=(total>total or 50<total)

#OUTPUT
print("#########################")
print("# Maderas:    EL CAJAMARQUINO")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# mesas:", mesas,"                            precio:  S/.", precio_de_una_mesa)
print("# sillas:", sillas,"                          precio:  S/.", precio_de_una_silla)
print("# carpetas:", carpetas,"                      precio:  S/.", precio_de_una_carpeta)
print("# total:    S/.", total)
print("#########################")
print("# precio de  venta:", precio_de_venta)
