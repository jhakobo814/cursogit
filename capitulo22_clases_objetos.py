#1
class persona:
    def __init__ (self, nombre, apellido, edad):
        self.nombre=nombre
        self.Apellido=apellido
        self.Edad=edad
    def mostrarpersona(self):
        print("Nombre: "+self.nombre)
        print("Apellido: "+self.Apellido)
        print("Edad: "+str(self.Edad))

print("Objetos Originales")
p1=persona("Alfredo","Moreno Muñoz",35)
p1.mostrarpersona()
p2=persona("Valeria","Moreno",1)
p2.mostrarpersona()
p1.Edad=40
p2.Apellido="Moreno Alegria"
print("")
print("Objetos Modificados")
p1.mostrarpersona()
p2.mostrarpersona()
print("")
print("Objeto tras Asignacion")
p1=p2
p1.mostrarpersona()
p2.mostrarpersona()

#2
class cordenada:
    def __init__ (self,x,y):
        self.X=x
        self.Y=y
    def mostrarcordenada(self):
        print("(",self.X,",",self.Y,")")

class cuadrado:
    def __init__ (self,v1,v2,v3,v4):
        self.V1=v1
        self.V2=v2
        self.V3=v3
        self.V4=v4
    def mostrarvertices(self):
        print("El Cuadrado esta compuesto por los siguientes vertices:")
        self.V1.mostrarcordenada()
        self.V2.mostrarcordenada()
        self.V3.mostrarcordenada()
        self.V4.mostrarcordenada()

print("")
v1=cordenada(1,1)
v2=cordenada(4,1)
v3=cordenada(4,4)
v4=cordenada(1,4)
cuadro=cuadrado(v1,v2,v3,v4)
cuadro.mostrarvertices()

#3
print("")
class personapublica:
    def __init__ (self,nombre,apellido,edad):
        self.Nom=nombre
        self.Ape=apellido
        self.Eda=edad

class personaprivada:
    def __init__ (self,nombre,apellido,edad):
        self.__Nom=nombre
        self.__Ape=apellido
        self.__Eda=edad
    def GetNom(self):
        return self.__Nom
    def GetApe(self):
        return self.__Ape
    def GetEda(self):
        return self.__Eda
    def SetNom(self,nombre):
        self.__Nom=nombre
    def SetApe(self,apellido):
        self.__Ape=apellido
    def SetEda(self,edad):
        self.__Eda=edad

publico=personapublica("Leonardo","Agudelo Dussan",37)
privado=personaprivada("Alana","Agudelo Zuniga",7)
print("PERSONA PUBLICA:")
print("Nombre: "+publico.Nom+" "+publico.Ape)
print("Edad:",str(publico.Eda))
print("PERSONA PRIVADA:")
print("Nombre:",privado.GetNom(),privado.GetApe())
print("Edad:",str(privado.GetEda()))
print("")
print("Modificacion de valores en ambos objetos.....")
publico.Ape="Moreno Moreno"
privado.SetApe("Mosquera Mosquera")
print("PERSONA PUBLICA:")
print("Nombre: "+publico.Nom+" "+publico.Ape)
print("Edad:",str(publico.Eda))
print("PERSONA PRIVADA:")
print("Nombre:",privado.GetNom(),privado.GetApe())
print("Edad:",str(privado.GetEda()))


#4
print("")
class cordenada2:
    def __init__ (self,x,y):
        self.__X=x
        self.__Y=y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X=x
    def SetY(self,y):
        self.__Y=y
        
class cuadrado2:
    def __init__ (self,v1,v2,v3,v4):
        self.__V1=v1
        self.__V2=v2
        self.__V3=v3
        self.__V4=v4
    def __mostrarcordenadaV1(self):
        print("(",self.__V1.GetX(),",",self.__V1.GetY(),")")
    def __mostrarcordenadaV2(self):
        print("(",self.__V2.GetX(),",",self.__V2.GetY(),")")
    def __mostrarcordenadaV3(self):
        print("(",self.__V3.GetX(),",",self.__V3.GetY(),")")
    def __mostrarcordenadaV4(self):
        print("(",self.__V4.GetX(),",",self.__V4.GetY(),")")
    def mostrarvertices2(self):
        print("El Cuadrado esta compuesto por los siguientes vertices:")
        self.__mostrarcordenadaV1()
        self.__mostrarcordenadaV2()
        self.__mostrarcordenadaV3()
        self.__mostrarcordenadaV4()

l1=cordenada2(1,1)
l2=cordenada2(5,1)
l3=cordenada2(5,5)
l4=cordenada2(1,5)
cuadro2=cuadrado2(l1,l2,l3,l4)
cuadro2.mostrarvertices2()


#5, 6
print("")
class person:
    def __init__ (self):
        self.__Nombre=""
        self.__Apellido=""
        self.__Edad=0
    def getnombre(self):
        return self.__Nombre
    def getapellido(self):
        return self.__Apellido
    def getedad(self):
        return self.__Edad
    def setnombre(self,nombre):
        self.__Nombre=nombre
    def setapellido(self,apellido):
        self.__Apellido=apellido
    def setedad(self,edad):
        self.__Edad=edad

class alumno(person):
    def __init__ (self):
        self.__Curso=""
        self.__Asignatura=""
    def getcurso(self):
        return self.__Curso
    def getasignatura(self):
        return self.__Asignatura
    def setcurso(self,curso):
        self.__Curso=curso
    def setasignatura(self,asignatura):
        self.__Asignatura=asignatura
    def mostraralumnos(self):
        print("Alumno:")
        print("\tNombre:",self.getnombre())
        print("\tApellido:",self.getapellido())
        print("\tEdad:",self.getedad())
        print("\tCurso:",self.__Curso)
        print("\tAsignatura:",self.__Asignatura)

class profesor(person):
    def __init__ (self):
        self.__Antiguedad=""
        self.__Tutorias=""
        self.__Telefono=""
    def getantiguedad(self):
        return self.__Antiguedad
    def gettutorias(self):
        return self.__Tutorias
    def gettelefono(self):
        return self.__Telefono
    def setantiguedad(self,antiguedad):
        self.__Antiguedad=antiguedad
    def settutorias(self,tutorias):
        self.__Tutorias=tutorias
    def settelefono(self,telefono):
        self.__Telefono=telefono
    def mostrarprofesor(self):
        print("Profesor")
        print("\tNombre:",self.getnombre())
        print("\tApellido:",self.getapellido())
        print("\tEdad:",self.getedad())
        print("\tAntiguedad:",self.__Antiguedad)
        print("\tTutorias:",self.__Tutorias)
        print("\tTelefono:",self.__Telefono)
    

estudiante=alumno()
estudiante.setnombre("Alfredo")
estudiante.setapellido("Moreno Muñoz")
estudiante.setedad(35)
estudiante.setcurso("Bachillerato")
estudiante.setasignatura(["Matematicas","Tecnologias","Ingles"])
estudiante.mostraralumnos()

maestro=profesor()
maestro.setnombre("Pablo")
maestro.setapellido("Casa Papel")
maestro.setedad(29)
maestro.setantiguedad(15)
maestro.settutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
maestro.settelefono("6544343")
maestro.mostrarprofesor()
    
