numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))

print("Resultado de la suma: ",numero1+numero2)

print("Resultado de la division: ",numero1/numero2)

print("Resultado de la division entera: ",numero1//numero2)

print("resultado de la potencia ",numero1**numero2)

numero3 = float(input("Primer numero: "))
numero4 = float(input("Sefundo numero: "))

print("Resultado de la Resta: ",numero3-numero4)

print("Resultado de la Division: ",numero3/numero4)

print("Resultado de Multiplicacion: ",numero3*numero4)

resultado = round(numero3*numero4,1)

print("Resultado de Multiplicacion redondeada: ",resultado)

numero5 = complex(float(input("Parte Real: ")),float(input("Parte Imaginaria: ")))
print(numero5)

numero6 = complex(float(input("Parte Real numero 2: ")),float(input("Parte Imaginaria numero 2: ")))

print("Resultado de la suma numero complejos: ",numero5+numero6)

numero10 = float(input("numero 1: "))
numero11 = float(input("numero 2: "))
numero12 = float(input("numero 3: "))
numero13 = float(input("numero 4: "))
numero14 = float(input("numero 5: "))
numero15 = float(input("numero 6: "))

resultado2 = (numero14+(numero12*(numero10**numero15)))-(numero13//numero11)
print("Resultado de la operacion: ", resultado2)
