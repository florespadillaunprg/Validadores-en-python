# INPUT
cliente=input("Ingrese el nombre del cliente:")
kg=int(input("Ingrese Nr Kg de camote:"))
precio_camote=float(input("Ingrese precio de cada camote:"))

# PROCESSING
total = (precio_camote * kg)

# VERIFICADOR
comprador=(total!=total)

# OUTPUT
print("#######################")
print("# CENTRO COMERCIAL DE TUBERCULOS")
print("#######################")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg camote")
print("# P.U.   :  S/.", precio_camote)
print("# Total  :  S/.", total)
print("#######################")
print("# comprador:", comprador)
