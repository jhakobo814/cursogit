def factorial(numero):
    if numero==1:
        return 1
    else:
        return numero*factorial(numero-1)

factori=int(input("Escribe el numero al que desea saber el factorial: "))
print("El factorial de: "+str(factori)+" es: "+str(factorial(factori)))


def potencia(base,exponente):
    if exponente<=0:
        return 1
    else:
        return base*potencia(base,exponente-1)

base=int(input("Escribe la base de la potencia: "))
exponente=int(input("Escribe el exponente de la potencia: "))
print("El valor de "+str(base)+" elevado a la "+str(exponente)+" es "+str(potencia(base,exponente)))
