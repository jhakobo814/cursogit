#1
print("Iniciamos el programa!!")
try:
    print(str(17/0))
except:
    print("Error Division por cero")
finally:
    print("primera parte terminada!")

print("\nComienza la segunda parte del codigo")

try:
    print(str(17/1))
except:
    print("Error Division por cero")
finally:
    print("segunda parte terminada")

#2
print("\n")
print("\nIniciamos el programa!!")
try:
    print(str(17/0))
except:
    print("Error Division por cero")
else:
    print("No se han producido errores")
finally:
    print("primera parte terminada!")

print("\nComienza la segunda parte del codigo")

try:
    print(str(17/1))
except:
    print("Error Division por cero")
else:
    print("No se han producido errores")
finally:
    print("segunda parte terminada")


#3
print("\n")
print("\nIniciamos el programa!!")
try:
    print(str(17/0))
except ZeroDivisionError:
    print("Error Division por cero")
except:
    print("Error General")
else:
    print("No se han producido errores")
finally:
    print("primera parte terminada!")
