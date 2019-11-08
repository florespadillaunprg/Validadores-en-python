# INPUT
cliente=input("Ingrese el nombre del cliente:")
DNI=int(input("Ingrese el numero de DNI:"))
arroz=int(input("Ingrese numero de kg de arroz:"))
fideo=int(input("Ingrese numero de kg de fideo:"))
azucar=int(input("Ingrese numero de kg de azucar:"))
precio_de_kg_arroz=float(input("Ingrese el precio de kg de arroz:"))
precio_de_kg_fideo=float(input("Ingrese el precio de kg de fideo:"))
precio_de_kg_azucar=float(input("Ingrese el precio de kg de azucar:"))

# PROCESSING
total=((arroz*precio_de_kg_arroz)+(fideo*precio_de_kg_fideo)+(azucar*precio_de_kg_azucar))

# VERIFICADOR
IGV=(total>=fideo and 52!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA AYACUCHANA")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# arroz:", arroz,"kg                               precio:   S/.", precio_de_kg_arroz)
print("# fideo:", fideo,"kg                               precio:   S/.", precio_de_kg_fideo)
print("# azucar:", azucar,"kg                             precio:   S/.", precio_de_kg_azucar)
print("# total:    S/.", total)
print("#########################")
print("# IGV:", IGV)
