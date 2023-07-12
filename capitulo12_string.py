cadena1 = "texto entre comillas dobles"
cadena2 = 'texto entre comillas simples'
print(cadena1)
print(cadena2)

cadena = "Python"
print("Caracter posision 0: ",cadena[0])
print("Caracter posision 1: ",cadena[1])
print("Caracter posision 2: ",cadena[2])
print("Caracter posision 3: ",cadena[3])
print("Caracter posision 4: ",cadena[4])
print("Caracter posision 5: ",cadena[5])

cadena3 = "leonardo" #input("Introduzca 1 string: ")
cadena4 = "agudelo"  #input("Introduzca 2 string: ")
cadena5 = "dussan"   #input("Introduzca 3 string: ")
cadenasuma = cadena3+" "+cadena4+" "+cadena5
cadenamulti = (cadena4 + " ") * 5
print("Carateres concatenados: ",cadenasuma)
print("Carateres multiplicados: ",cadenamulti)


cadena6 = "Python" #input("Introduzca el 1 String: ")
cadena7 = "th"     #input("Introduzca el 2 String: ")
print("Esta el segundo string contenido en el primero: ",cadena7 in cadena6)

cadena8 = "leonardo" #input("Introduzca 1 string: ")
cadena9 = "agudelo"  #input("Introduzca 2 string: ")
cadena10 = "dussan"  #input("Introduzca 3 string: ")
cadenaconsaltos = "\n\t"+cadena8+"\n\t"+cadena9+"\n\t"+cadena10
print("cadena con saltos:",cadenaconsaltos)
cadenaconsaltos = r"\n\t"+cadena8+r"\n\t"+cadena9+r"\n\t"+cadena10
print("cadena con saltos:",cadenaconsaltos)

print("")
string1 ="leonardo"    #input("introduzca el primer String: ")
string2 = "agudelo"     #input("introduzca el segundo String: ")
string3 = "dussan"      #input("introduzca el tercer String: ")
string4 = "alana agudelo zuniga"
print("Los tres String introducidos son: ","\n\t"+"String1: "+string1+"\n\t"+"String2: "+string2+"\n\t"+"String3: "+string3)
print("Cuarto String:",string4)
print("Longitud del String2: ",len(string2))
print("String3 todo a Mayuscula: ",string3.upper())
print("String3 todo a Minuscula: ",string3.lower())
print("String2 cambia de May a Min y Veceversa: ",string2.swapcase())
print("String1 la primera a May: ",string1.capitalize())
print("String4 la primera de cada palabra a MAY: ",string4.title())
print("El String1 es todo minuscula:",string1.islower())
print("El String3 es todo mayuscula:",string1.isupper())
print("String2 todo caracter es imprimible:",string2.isprintable())
print("String1 todos caracteres son alfanumericos",string1.isalnum())
print("String1 todos caracteres son alfabeticos",string1.isalpha())
print("String4 es la primera letra de cada palabra en MAY?:",string4.istitle())
print("String4 todos los caracteres son espacios en blanco?:",string4.isspace())
print("string1 todo digitos?:",string1.isdigit())
print("String2 todos los caracteres con representacion numerica?:",string2.isnumeric())
print("String3 todos los caracteres son numero con representacion decimal?:",string3.isdecimal())
print("Caracter mas alto del String1:",max(string1))
print("caracter mas bajo del string3:",min(string3))

print("")
string5 = " yo soy tanos "
print("El string 5 ingresado es:",string5)
print("longitud del String",len(string5))
stringstrip = string5.lstrip()
print("String lstrip:",stringstrip,end=".")
print("\nLongitud del string",len(stringstrip))
stringstrip2 = stringstrip.rstrip()
print("String rstrip:",stringstrip2,end=".")
print("\nLongitud del string",len(stringstrip2))
stringstrip3 = string5.strip()
print("String strip:",stringstrip3,end=".")
print("\nLongitud del string",len(stringstrip3))

string6 = "me encanta programar en Python"
print("El string 6 ingresado es:",string6)
buscar = "m"
print("String a buscar \"m\":")
print("Empieza el string6 por \"m\":",string6.startswith(buscar))
print("Termina el string6 por \"m\":",string6.endswith(buscar))
print("Cuantas veces aparece \"m\" en el string6:",string6.count(buscar))
buscar2 = "a"
print("el string \"a\" aparece en la primera posicion:",string6.find(buscar2))
print("el string \"a\" aparece en la ultima posicion:",string6.rfind(buscar2))

string7 = "la casa es de color blanco"
print("El string 7 ingresado es:",string7)
reemplazar = "co"
print("El texto que se va a reemplaza: \"co\"")
reemplazo = "TA"
print("El texto que se va a intoruccir: \"TA\"")
print("Nuevo string:",string7.replace(reemplazar,reemplazo))

print("Spring7 dividido por espacios en blanco",string7.split())

string8 = "F.C.Barselona, Atletico de Madrid, Real Madrid"
print("El string8 introduccido:",string8)
print("Primer equipo:",string8[0:13])
print("Segundo equipo:",string8[15:33])
print("Tercer equipo:",string8[35:46])
print("Desde el principio:",string8[:13])
print("Desde el final:",string8[15:])

multiplicando = 20
multiplicador = 10
print("El resultado del multiplicar %d por %d es %d"%(multiplicando, multiplicador, multiplicando*multiplicador))

print("El resultado del multiplicar {0} por {1} es {2}". format(multiplicando, multiplicador, multiplicando*multiplicador))

print(f"Mi nombre es: {cadenasuma}")
print("Mi nombre es: {0}". format(cadenasuma))



