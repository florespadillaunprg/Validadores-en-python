# INPUT
cliente=input("Ingrese nombre del cliente:")
numero_de_DNI=int(input("Ingrese numero de DNI:"))
numero_de_RUC=int(input("Ingrese numero de RUC:"))
kg_de_pollo=int(input("Ingrese el numero de kg de pollo:"))
kg_de_res=int(input("Ingrese el numero de kg de papa:"))
precio_de_kg_de_pollo=float(input("Ingrese el precio de kg de pollo:"))
precio_de_kg_de_res=float(input("Ingrese el precio de kg de res:"))

# PROCESSING
total=((kg_de_pollo*precio_de_kg_de_pollo)+(kg_de_res*precio_de_kg_de_res))

# VERIFICADOR
venta=(kg_de_res>kg_de_pollo)

#OUTPUT
print("#########################")
print("# CARNICERIA:   EL CHATO ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", numero_de_DNI)
print("# RUC:", numero_de_RUC)
print("# pollo:", kg_de_pollo,"kg                      precio:  S/.", precio_de_kg_de_pollo)
print("# res:", kg_de_res,"kg                          precio:  S/.", precio_de_kg_de_res)
print("# total: S/.",total)
print("#########################")
print("# venta:", venta)
