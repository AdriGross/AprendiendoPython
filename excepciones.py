# ***** PRACTICA SOBRE MANEJO DE EXCEPCIONES *****

print(3/0)

try:
    print(3/0)
except:
    print("ERROR: Division por cero")

print("¡Iniciando programa!")
try:
    print(3/0)
except:
    print("ERROR: Division erronea")
finally:
    print("¡Programa acabado!")

print("¡Iniciando programa!")
try:
    print(3/1)
except:
    print("ERROR: Division erronea")
finally:
    print("¡Programa acabado!")

print("¡Iniciando programa!")
try:
    print(3/1)
except:
    print("ERROR: Division erronea")
else:
    print("¡No se han producido errores!")
finally:
    print("¡Programa acabado!")

print("¡Iniciando programa!")
try:
    print(3/0)
except ZeroDivisionError:
    print("ERROR: Division por cero")
except:
    print("ERROR General")
else:
    print("¡No se han producido errores!")
finally:
    print("¡Programa acabado!")