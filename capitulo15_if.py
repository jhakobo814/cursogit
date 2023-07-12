numero=int(input("Escriba un numero del 1 al 1000: "))
if numero>400:
    print("El numero es mayor que 400!")
print("Has escrito el numero "+str(numero))

cadena=input("Introduzca la cadena de texto: ")
if cadena.endswith("a") or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
    print("La cadena introduccida termina en vocal!!")
print("has escrito la cadena",cadena)

numero1=int(input("Escriba numero de 1 al 1000: "))
if numero1<400:
    print("El numero que has escrito es menor a 400!")
else:
    print("El numero que has escrito es mayor o igual a 400!")
print("has estrito",numero1)

sumando1=int(input("Escriba el primer numero: "))
sumando2=int(input("Escriba el segundo numero: "))
resultado=sumando1+sumando2
print("El resultado de la suma es: "+str(resultado))
if resultado%2==0:
    if resultado>=1000:
        print("El resultado de la suma es par y mayor o igual que 1000!")
    else:
        print("El resultado de la suma es par y menor que 1000!")
else:
    if resultado>=1000:
        print("El resulatado de la suma es impar y mayor o igual que 1000!")
    else:
        print("El resultado de la suma es impar y menor que 1000!")

numero2=int(input("Escriba el primer numero: "))
numero3=int(input("Escriba el segundo numero: "))
if numero2==numero3:
    print("Ambos numeros son iguales")
elif numero2>numero3:
    print("El primer numero es mayor que el segundo")
else:
    print("El segundo numero es mayor que el primero")


