Wendy Nayerly Panameño Riascos
Miguel Ángel arboleda Pérez
Johan Steinert Riascos Panameño
Hellen Johana Sinisterra Gonzalez
Yeisy Samara Minota cortes


mensaje=("Bienvenido a la clase de Algoritmia y Programacion")

print(mensaje)
cadena=("Bienvenido a la clase de Algoritmia y Programacion")
print(cadena)

nombre=input("Poner nombre:")
print("Hola "+ nombre + " Bienvenido a la clase dse Algoritmia y Programacion")

Nhoras=int(input("Horas trabajadas:"))
CosteH=int(input("Coste Horas:"))
PagoH=Nhoras*CosteH
print("El pago correspondiente a las horas es:", PagoH)

numero=int(input("Numero Entero:"))
suma=numero*(numero +1)/2
print("La suma de los primeros numeros enteros desde la 1 hasta "+str(numero)+ " es " +str(suma))

peso=float(input("Digitar peso:"))
altura=float(input("Digitar Altura:"))
imc=round(peso/(altura*altura),2)
print("su imc es de:",imc)

n=input("Introducir Dividendo Entero:")
m=input("Introducir Divisor Entero:")
print(n + " entre " + m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))


Cantidad=float(input("Cantidad a Invertir:"))
interes=float(input("Interes de porcentaje actual:"))
años=int(input("¿Años:?"))
print("Cantidad final:" + strround(cantidad +(interes/100 + 1)**años,2))))



PesoC=str(input("Introducir peso de Carros:"))
PesoA=str(input("Introducir peso de Aviones:"))
PesoB=str(input("Introducir peso de Balones:"))
PesoT=PesoC+PesoA+PesoB
print("El peso total es:" ,PesoT      
































name=input("¿Como te llamas?:")
print(name.lower())
print(name.upper())
print(name.title())

nombre=input("¿Como te llamas?:")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras ")

frase=input("Introduce una frase:")
print(frase[::-1])

frase=input("introduce una frase:")
vocal=input("Introduce una vocal:")
print(frase.replace(vocal, vocal.upper()))


email=input("Introduce tu correo electronico:")
print( email[:email.find("@")] + "@sigma7.com.co")

fecha=input("02/03/2012")
print("dia", fecha[:2])
print("mes", fecha[:3])
print("año", fecha[2012])











producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))
print("{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€".format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))


cesta = input('Introducir producto: ')
print(cesta.replace(',', '\n'))