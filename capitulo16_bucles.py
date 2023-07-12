lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for item in lista:
    print(item, end=" ")

print("\n")    
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
interaciones=[1,2,3,4,5]
for x in interaciones:
    print("interaciones numero: "+str(x))
    for y in abc:
        print(y, end=",")
    print("\n")
    
lista2=[99,"casa",["hola","adios"],"perro","gato",34]
for x in lista2:
    print(x)
    
for x in range(5):
    for y in range(3):
        print("Iteracion "+str(x)+","+str(y))
    
i=0
while i<10:
    print(i, end=" ")
    i=i+1

print("\n")
pedirnumero=True
while pedirnumero:
    valor=int(input("Escribe un numero menor a 10: "))
    if valor<10:
        pedirnumero=False
print("Fin, has escrito un numero menor a 10: "+str(valor))

i=0
while i<5:
    j=0
    while j<3:
        print("Iteracion "+str(i)+","+str(j))
        j=j+1
    i=i+1

print("\n")
for y in range(5):
    i=0
    while i<3:
        print("Iteracion "+str(y)+","+str(i))
        i=i+1
    
