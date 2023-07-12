
#Listas
lista = ["python","RA-MA","2019","Libro",3]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print("")
lista1 = ["Camiseta","Pantalon","Zapatillas"]
lista2 = ["Abrigo","Jersey","Sudadera","Calcetiles"]
print("Numero de elementos de la lista 1:",len(lista1))
print("lista1:",lista1)
print("Numero de elementos de la lista 2:",len(lista2))
print("lista2:",lista2)
lista_concatenada = lista1+lista2
print("Numero de elemtos de la lista concatenada:",len(lista_concatenada))
print("Lista concatenada:",lista_concatenada)

print("")
lista3 = ["Camiseta","Pantalon","Zapatillas"]
print(lista3)
lista3 = lista3+["Abrigo"]
print(lista3)
lista3 = lista3+["Jersey","sudadera"]
print(lista3)
lista3 = lista3+["Calcetines"]+["Bufanda"]
print(lista3)

print("")
lista4 = ["Camiseta","Pantalon","Zapatilla"]
print("lista4:",lista4)
lista4[1] = "Cazadora"
print(lista4)
del lista4[0]
print(lista4)

print("")
lista5 = ["Camiseta","Pantalon","Zapatilla"]
print(lista5)
lista5resultante = lista5*3
print(lista5resultante)

print("")
lista6 = ["Camiseta", ["Calcetinez","Cazadora"],"Zapatilla"]
print(lista6)
print(lista6[0])
print(lista6[1])
print(lista6[2])
print(lista6[1][0])
print(lista6[1][1])

print("")
lista7 = [1,2,3,4,5,6,7,8,9]
print(lista7)
lista8 = lista7[3:7]
print(lista8)
lista9 = lista7[:5]
print(lista9)
lista10 = lista7[6:]
print(lista10)

print("")
lista11 = [45,32,3,78]
print("Lista Original",lista11)
lista11.append(995)
lista11.append(7)
print("lista despues de usar append",lista11)
lista11.sort()
print("lista ordenada sort",lista11)
lista11.reverse()
print("Lista invertida",lista11)
listaextend = [1,5,87,45]
lista11.extend(listaextend)
print("lista extend",lista11)
lista11.sort(reverse=True)
print("lista ordenada e invertida",lista11)
print("numero de elementos 45:",lista11.count(45))
lista11.insert(4,111)
print("lista despues de insert:",lista11)
lista11.remove(45)
print("lista despues de remove:",lista11)
print("posicion del elemnto 111:",lista11.index(111))
lista11.pop()
print("lista despues de pop:",lista11)
lista11.clear()
print("lista despues del clear:",lista11)

#Tuplas
print("")
tupla=("casa","2",99,"perro",99)
print("Elementos de la tupla:",tupla)
print("Elemento de la posicion[0]:",tupla[0])
print("Elemento de la posicion[1]:",tupla[1])
print("Elemento de la posicion[2]:",tupla[2])
print("Elemento de la posicion[3]:",tupla[3])
print("Elemento de la posicion[4]:",tupla[4])
print("Numero de elementos 99:",tupla.count(99))
print("Posicion que ocupa el elemento Perro:",tupla.index("perro"))

print("")
tupla2=(1,2,3,4,5,6,7,8,9)
print(tupla2)
print(tupla2[4:9])
print(tupla2[:3])
print(tupla2[2:])

print("")
tupla3=(29,"tv",8763)
tupla4=(1,2,3,"videogame")
print("tupla3:",tupla3)
print("numero de elementos de la tupla3:",len(tupla3))
print("tupla4:",tupla4)
print("numero de elementos de la tupla4:",len(tupla4))
tuplaconcatenada=tupla3+tupla4
print("tupla concatenada:",tuplaconcatenada)
print("numero de elementos de la tupla concatenada:",len(tuplaconcatenada))

print("")
tupla5=(1,2,3,4,5,6,7,8,9,0)
print(tupla5)
tuplaresultado=tupla5*4
print(tuplaresultado)

#Diccionarios
print("")
diassemana={"lunes":"monday",
            "martes":"tuesday",
            "miercoles":"wednesday",
            "jueves":"thursday",
            "viernes":"friday"}
print(diassemana["lunes"])
print(diassemana["miercoles"])
print(diassemana["viernes"])
print("\n--------------------------------------------------------------------------------")
print("aqui estoy imprimiendo el diccionario", diassemana)              ############################################
#print(diassemana)
print("\n--------------------------------------------------------------------------------")
diassemana["sabado"]="saturday"
print(diassemana)
diassemana["domingo"]="sunday"
print(diassemana)
diassemana["lunes"]="mondayBORRAR"
print(diassemana)
del diassemana["lunes"]
print(diassemana)
print("Numero de elementos del diccionario:",len(diassemana))
print("Elemento mayor del diccionario:",max(diassemana))
print("Elemento  menor del diccionario",min(diassemana))

print("")
semana={"lunes":"monday",
        "martes":"tuesday",
        "miercoles":"wednesday",
        "jueves":"thursday",
        "viernes":"friday"}
print("Diccionario original:",semana)
copiasemana=semana.copy()
print("Diccionario Copia:",copiasemana)
print("Valor del lunes (pop):",semana.pop("lunes"))
print("Diccionario despues del pop:",semana)



