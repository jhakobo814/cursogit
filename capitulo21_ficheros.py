#1
f=open("fichero.txt","r")
texto=f.read()
print(texto)
f.close()

#2
print("")
for linea in open("fichero.txt","r"):
    print(linea)

#3
print("")
a=open("fichero.txt","r")
print(a.readline())
print(a.readline())
print(a.readline())
print(a.readline())
a.close()

#4
print("")
b=open("fichero.txt","r")
lineas=b.readlines()
b.close()
print(lineas[0])
print(lineas[1])
print(lineas[2])
print(lineas[3])
print(lineas[4])
j=0
for i in lineas:
    print("linea "+str(j)+": "+str(i))
    j=j+1

#5
print("")
c=open("fichero.txt","r")
linea=list(c)
c.close()
for item in linea:
    print(item)

#6 Adicionar lineas a un fichero existente
print("")
print("fichero Inicial")
flectura=open("fichero.txt","r")
texto1=flectura.read()
flectura.close()
print(texto1)
print("Insertando linea...\n")
fescritura=open("fichero.txt","a")
fescritura.write("\nNueva linea en el fichero")
fescritura.close()
print("Fichero inicial")
flectura=open("fichero.txt","r")
texto1=flectura.read()
flectura.close()
print(texto1)


#7 Crear un fichero nuevo
print("")
#fcrear=open("nuevofichero.txt","x")
#fcrear.write("Estoy aprendiendo Python..\n")
#fcrear.write("...y me encanta.\n")
#fcrear.write("Me parece un lenguaje de programacion\n")
#fcrear.write("muy facil de aprender\n")
#fcrear.close()

print("Nuevo fichero creado")
fflectura=open("nuevofichero.txt","r")
texto=fflectura.read()
fflectura.close()
print(texto)


#8 Utilizar un fichero creado, eliminar el contenido y volver a escribir
fcrear1=open("nuevofichero.txt","w")
fcrear1.write("Fichero creado desde cero\n")
fcrear1.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
fcrear1.write("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n")
fcrear1.write("sdfsdfsdfs dfsfsdf sdfs dfsd fas gasdg dfgdsf gdfg sdg dsfgsd fgsdfg sdfgsd fgsdf gsdfg dsfg sdf\n")
fcrear1.close()

print("### Fichero creado ###")
f1lectura=open("nuevofichero.txt","r")
texto=f1lectura.read()
f1lectura.close()
print(texto)
