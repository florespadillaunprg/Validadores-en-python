# INPUT
cliente=input("Ingrese el nombre del cliente:")
DNI=int(input("Ingrese el numero de DNI:"))
RUC=int(input("Ingrese el numero de RUC:"))
gaseosas=int(input("Ingres la cantidad de gaseosas:"))
cervezas=int(input("Ingrese el numero de cervezas:"))
cifruts=int(input("Ingrese el numero de cifruts:"))
precio_de_una_gaseosa=float(input("Ingrese el precio de una gaseosa:"))
precio_de_una_cerveza=float(input("Ingrese el precio de una cerveza:"))
precio_de_un_cifrut=float(input("Ingrese el precio de un cifrut:"))

# PROCESSING
total=((gaseosas*precio_de_una_gaseosa)+(cervezas*precio_de_una_cerveza)+(cifruts*precio_de_un_cifrut))

# VERIFICADOR
cantidad_de_bebida=not(total!=gaseosas or total==total)

#OUTPUT
print("#########################")
print("# Centro comercial:     MI JUANITA  ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# RUC:", RUC)
print("# gaseosas:", gaseosas,"                        precio:   S/.", precio_de_una_gaseosa)
print("# cervezas:", cervezas,"                        precio:   S/.", precio_de_una_cerveza)
print("# cifruts:", cifruts,"                          precio:   S/.", precio_de_un_cifrut)
print("# total:   S/.", total)
print("#########################")
print("# cantidad de bebida:", cantidad_de_bebida)
