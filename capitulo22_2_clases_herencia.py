#7
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
    
class investigador(person):
    def __init__ (self):
        self.__Especialidad=""
        self.__Anos=""
    def getespecialidad(self):
        return self.__Especialidad
    def getanos(self):
        return self.__Anos
    def setespecialidad(self,especialidad):
        self.__Especialidad=especialidad
    def setanos(self,anos):
        self.__Anos=anos

class profesoruniversitario(profesor,investigador):
    def __init__ (self):
        self.__Universidad=""
        self.__Departamento=""
    def getuniversidad(self):
        return self.__Universidad
    def getdepartamento(self):
        return self.__Departamento
    def setuniversidad(self,universidad):
        self.__Universidad=universidad
    def setdepartamento(self,departamento):
        self.__Departamento=departamento
    def mostrarprofesoruniversitario(self):
        print("Profesor Universitarop")
        print("\tNombre:",self.getnombre())
        print("\tApellido:",self.getapellido())
        print("\tEdad:",self.getedad())
        print("\tAntiguedad:",self.getantiguedad())
        print("\tTutorias:",self.gettutorias())
        print("\tTelefono:",self.gettelefono())
        print("\tEspecialidad:",self.getespecialidad())
        print("\tAños:",self.getanos())
        print("\tUniversidad:",self.__Universidad)
        #print("\tDepartamento:",self.__Departamento) esta forma o la que sigue.
        print("\tDepartamento:",self.getdepartamento())
        

maestro=profesoruniversitario()
maestro.setnombre("Alfredo")
maestro.setapellido("Moreno Muñoz")
maestro.setedad(35)
maestro.setantiguedad(15)
maestro.settutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
maestro.settelefono("6544343")
maestro.setespecialidad("Desarrollo de Software")
maestro.setanos(15)
maestro.setuniversidad("Universidad de Extremadura")
maestro.setdepartamento("Lenguaje y Sistemas Informaticos")
maestro.mostrarprofesoruniversitario()
