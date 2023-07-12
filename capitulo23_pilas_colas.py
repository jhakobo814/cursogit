class Pila:
    def __init__ (self):
        self.__items=[]

    def estavacia(self):
        if len(self.__items)==0:
            return True
        else:
            return False

    def apilar(self,item):
        self.__items.append(item)

    def retirar(self):
        return self.__items.pop()

    def leercima(self):
        return self.__items[len(self.__items)-1]

    def numeroelementos(self):
        return len(self.__items)

    def mostrarpila(self):
        print("Pila: ",self.__items,"<--Cima")

def simuladorpila():
    fin=False
    pila=Pila()
    while not(fin):
        opc=input("Opcion:")
        if (opc=="1"):
            item=input("Indroduzca el elemento a apilar: ")
            pila.apilar(item)
            print("Elemento apilado:",item)
        elif (opc=="2"):
            if pila.estavacia():
                print("La pila esta vacia, no puede retirarce ningun elemento")
            else:
                item=pila.leercima()
                pila.retirar()
                print("Elemento retirado:",item)
        elif (opc=="3"):
            if pila.estavacia():
                print("La pila esta vacia, no puede leerse de encima")
            else:
                print("La cima es:",pila.leercima())
        elif (opc=="4"):
            print("La pila tiene:",pila.numeroelementos()," elementos")
        elif (opc=="5"):
            if pila.estavacia():
                print("La pila esta Vacia")
            else:
                print("La pila no esta Vacia")
        elif (opc=="6"):
            pila.mostrarpila()
        elif (opc=="7"):
            fin=True

print("""***************
Simulador de Pila
*****************
Menu
1) Apilar
2) Retirar
3) Leer Cima
4) Numero de Elementos
5) Esta Vacia?
6) Mostrar Pila
7) Salir""")
simuladorpila()


    
        
        
