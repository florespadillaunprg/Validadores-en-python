# INPUT
cliente=input("Ingrese el nombre del cliente:")
RUC=int(input("Ingrese el numero de RUC:"))
baldes=int(input("Ingrese la cantidad de baldes:"))
tinas=int(input("Ingrese la cantidad de tinas:"))
cilindros=int(input("Ingrese la cantidad de cilindros:"))
precio_de_un_balde=float(input("Ingrese el precio de un balde:"))
precio_de_una_tina=float(input("Ingrese el precio de una tina:"))
precio_de_un_cilindro=float(input("Ingrese el precio de un cilindro:"))

# PROCESSING
total=((baldes*precio_de_un_balde)+(tinas*precio_de_una_tina)+(cilindros*precio_de_un_cilindro))

# VERIFICADOR
ganancia=(total==total)

#OUTPUT
print("#########################")
print("# Plastiqueria:      RAMOS  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# baldes:", baldes,"                                       precio:   S/.", precio_de_un_balde)
print("# tinas:", tinas,"                                         precio:   S/.", precio_de_una_tina)
print("# cilindros:", cilindros,"                                 precio:   S/.", precio_de_un_cilindro)
print("total:     S/.", total)
print("#########################")
print("# ganancia:", ganancia)
