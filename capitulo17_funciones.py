#1
def hola():
    print("Hola!, te gusta python?")
print("primera invocacion: ",end="")
hola()
print("segunda invocacion: ",end="")
hola()
print("")


#2
def hola1():
    return "Hola Si te gusto?"
print("Primera invocacion: "+hola1())
print("Segunda invocacion: "+hola1())
print("")


#3
def parimpar(param):
    if param%2==0:
        print("El numero es par:",param)
    else:
        print("El numero es impar:",param)

numero=int(input("Escribe un numero: "))
parimpar(numero)
print("")


#4
def multi(num1,num2):
    return num1*num2

numero1=int(input("Escribe el multiplicando: "))
numero2=int(input("Escribe el multiplicador: "))
resultado=multi(numero1,numero2)
print("El resultado de la multiplicacion es:",resultado)
print("")


#5
def suma(*valores):
    resultado1=0
    for x in valores:
        resultado1=resultado1+x
    return resultado1

resultado1=suma(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es:",resultado1)
print("")


#6
def sumamulti(*valores):
    resultadosuma=0
    resultadomulti=1
    for i in valores:
        resultadosuma=resultadosuma+i
        resultadomulti=resultadomulti*i
    return resultadosuma,resultadomulti

ressuma,resmulti=sumamulti(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es:",ressuma)
print("El resultado de la multiplicacion es:",resmulti)
print("")


#7
def sumamulti2(param1,param2):
    return sumar(param1,param2),multi(param1,param2)

def sumar(sumando1,sumando2):
    return sumando1+sumando2

#La funcion multi() ya estaba creada arriba

numero3=int(input("Escribe el primer numero: "))
numero4=int(input("Escribe el segundo numero: "))

resultasuma,resultamulti=sumar(numero3,numero4),multi(numero3,numero4)
print("El resultado de la suma es:",resultasuma)
print("El resultado de la multiplicacion es:",resultamulti)
print("")

#Variables globales
#8
def variables():
    variable=3
    print("Valor dentro de la funcion: "+str(variable))

variable=5
variables()
print("Variable en el programa principal: "+str(variable))
print("")

#9
def variables2():
    global variable1
    print("Valor dentro de la funcion: "+str(variable1))
    variable1=3
    print("Nuevo Valor dentro de la funcion: "+str(variable1))

variable1=5
print("Variable en el codigo principal: "+str(variable1))
variables2()
print("Variable en el codigo principal: "+str(variable1))
