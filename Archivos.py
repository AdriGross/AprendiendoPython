# ***** PRACTICA SOBRE MANEJO DE ARCHIVOS *****

f = open("prueba.txt", "r")
texto = f.read()
print(texto)
f.close()

for linea in open("prueba.txt", "r"):
    print(linea)

f = open("prueba.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("prueba.txt", "r")
lineas = f.readlines()
f.close()
print(lineas[0])
print(lineas[1])
print(lineas[2])
print(lineas[3])

f = open("prueba.txt", "r")
lineas = list(f)
f.close()
for item in lineas:
    print(item)

print("###Archivo original###")
flectura = open("prueba.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)
print("###Insertando linea...###\n")
fescritura = open("prueba.txt", "a")
fescritura.write("\nSigo programando")
fescritura.close()
print("###Archivo modificado###")
flectura = open("prueba.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)

fcrear = open("pruebacreacion.txt", "x")
fcrear.write("Sigo aca\n")
fcrear.write("Archivo creado hoy\n")
fcrear.close()
print("###Archivo creado###")

flectura = open("pruebacreacion.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)

fcrear = open("pruebacreacion.txt", "w")
fcrear.write("Archivo creado desde cero\n")
fcrear.write("Sigo aca\n")
fcrear.write("Archivo creado hoy\n")
fcrear.close()
print("###Archivo creado###")

flectura = open("pruebacreacion.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)