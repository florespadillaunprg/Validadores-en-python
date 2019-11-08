# INPUT
cliente=input("Ingrese el nombre del cliente:")
numero_de_venta=int(input("Ingrese el numero de venta:"))
libro01=input("Ingrese el nombre del libro01:")
libro02=input("Ingrese el nombre del libro02:")
libro03=input("Ingrese el nombre del libro03:")
precio_del_libro01=float(input("Ingrese el precio del libro01:"))
precio_del_libro02=float(input("Ingrese el precio del libro02:"))
precio_del_libro_03=float(input("Ingrese el precio del libro03:"))

# PROCESSING
total=(precio_del_libro01+precio_del_libro02+precio_del_libro_03)

# VERIFICADOR
total_comprado=not(total<3 or precio_del_libro_03>=3)

#OUTPUT
print("#########################")
print("# Libreria:   EL PERUANITO ")
print("#########################")
print("# cliente:", cliente)
print("# numero de venta:", numero_de_venta)
print("# libro:", libro01,"               precio: S/.", precio_del_libro01)
print("# libro:", libro02,"               precio: S/.", precio_del_libro02)
print("# libro:", libro03,"               precio: S/.", precio_del_libro_03)
print("# total: S/.", total)
print("#########################")
print("# total comprado:", total_comprado)
