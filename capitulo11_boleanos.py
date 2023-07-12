verdadero = True
falso = False
print("Valor de la variable verdadero: ",verdadero)
print("Valor de la variable falso: ",falso)

print("Resultado entre True AND False:  ", True and False)
print("Resultado entre True AND True:   ", True and True)
print("Resultado entre False AND False: ", False and False)
print("Resultado entre False AND True:  ", False and True)

print("Resultado entre True OR False:  ", True or False)
print("Resultado entre True OR True:   ", True or True)
print("Resultado entre False OR False: ", False or False)
print("Resultado entre False OR True:  ", False or True)

print("Resultado de NOT True:  ", not True)
print("Resultado de NOT False: ", not False)

booleano1 = bool(input("Primer Valor:  "))
booleano2 = bool(input("Segundo Valor: "))
booleano3 = bool(input("Tercer Valor:  "))
booleano4 = bool(input("Cuarto Valor:  "))
booleano5 = bool(input("Quinto Valor:  "))
print("Resultado",booleano4 or ((booleano3 and not booleano2) and booleano1) or boolean5)

numero1 = float(input("Numero 1:"))
numero2 = float(input("Numero 2:"))
numero3 = float(input("Numero 3:"))
numero4 = float(input("Numero 4:"))
print(numero1,"==",numero4,":",numero1==numero4)
print(numero2,"!=",numero3,":",numero2!=numero3)
print(numero3,">",numero2,":",numero3>numero2)
print(numero4,"<",numero1,":",numero4<numero1)
print(numero1,">=",numero3,":",numero1>=numero3)
print(numero2,"<=",numero4,":",numero2<=numero4)
