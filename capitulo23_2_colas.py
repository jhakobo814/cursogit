class Cola:
    def __init__(self):
        self.__items=[]

    def estavacia(self):
        if len(self.__items)==0:
            return True
        else:
            return False

    def encolar(self,item):
        self.__items.insert(0,item)

    def desencolar(self):
        return self.__items.pop()

    def leerprimerelemento(self):
        return self.__items[len(self.__items)-1]

    def numeroelementos(self):
        return len(self.__items)

    def mostrarcola(self):
        print("Cola:",self.__items,"<-- Primer elemento")

def simuladorcola():
    fin=False
    cola=Cola()
    while not(fin):
        opc=input("Opcion:")
        if (opc=="1"):
            item=input("Introduzca elementos a encolar:")
            cola.encolar(item)
            print("Elemento encolado:",item)
        elif (opc=="2"):
            if cola.estavacia():
                print("La cola esta vacia, no puede desencolar ningun elemento")
            else:
                item=cola.leerprimerelemento()
                cola.desencolar()
                print("Elemento desencolado",item)
        elif (opc=="3"):
            if cola.estavacia():
                print("La cola esta vacia, no puede leer ningun elemento")
            else:
                print("El primer elemento es:",cola.leerprimerelemento())
        elif (opc=="4"):
            print("La cola tiene",cola.numeroelementos()," elementos")
        elif (opc=="5"):
            if cola.estavacia():
                print("La cola esta vacia")
            else:
                print("La cola no esta vacia")
        elif (opc=="6"):
            cola.mostrarcola()
        elif (opc=="7"):
            fin=1

print("""***************
Simulador de Cola
*****************
Menu
1) Encolar
2) Desencolar
3) Leer el primer elemento
4) Numero de Elemteos
5) Esta Vacia?
6) Mostrar cola
7) Salir""")
simuladorcola()
        
    
