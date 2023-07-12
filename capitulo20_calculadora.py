def sumar():
    sum1=int(input("Primer numero a sumar: "))
    sum2=int(input("Segundo numero a sumar: "))
    print("La suma es:",sum1+sum2)
    
def resta():
    res1=int(input("Minuendo: "))
    res2=int(input("Sustraendo: "))
    print("La resta es:",res1-res2)

def multi():
    multi1=int(input("Multiplicando: "))
    multi2=int(input("Multiplicador: "))
    print("La multiplicacion es: ",multi1*multi2)

def dividir():
    try:
        divi1=int(input("Dividendo: "))
        divi2=int(input("Divisor: "))
        print("La division es:",divi1/divi2)
    except:
        print("Error: No se puede dividir por cero!")
        
def factorial():
    facto=int(input("Escriba numero para calcular factorial: "))
    print("El factorial de: "+str(facto)+" es "+str(factorialcalculo(facto)))

def factorialcalculo(numero):
    if numero<=1:
        return 1
    else:
        return numero*factorialcalculo(numero-1)

def potencia():
    base=int(input("Escriba la base de la potencia: "))
    expone=int(input("Escriba el exponente: "))
    print("El valor de: "+str(base)+" elevado a la "+str(expone)+" es: "+str(potenciacalculo(base,expone)))

def potenciacalculo(base,expone):
    if expone<=0:
        return 1
    else:
        return base*potenciacalculo(base,expone-1)

def calculadora():
    fin=False
    while not(fin):
        print("")
        #menu()
        opc=int(input("Opcion: "))
        if (opc==1):
            sumar()
        elif (opc==2):
            resta()
        elif (opc==3):
            multi()
        elif (opc==4):
            dividir()
        elif (opc==5):
            factorial()
        elif (opc==6):
            potencia()
        elif (opc==7):
            menu()
        elif (opc==8):
            fin=True
            print("Fin!!")

def menu():
    print("""***********
Calculadora
***********
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Factorial
6) Potencia
7) Repetir Menu
8) Salir""")

#inicio
menu()
calculadora()
