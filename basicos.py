print('hola mundo', "soy adriana")

print("lauti")

print(1, 2, 3, 4, 5, sep=".")

print(1, 2, 3, 4, 5, sep=".", end=".")

print("bienvenido, como te llamas?")
nombre = input()
print("gracias por elegirme", nombre)
edad = input("cuantos anios tienes?:")
print("tienes", edad, "anios.")

sumando1 = int(input("ingrese el primer numero:"))
sumando2 = int(input("ingrese el segundo numero:"))
print("resultado de la suma:", sumando1 + sumando2)
sumando1 = float(input("ingrese primer numero(decimal):"))
sumando2 = float(input("ingrese segundo numero(decimal):"))
print("resultado de la suma", sumando1 + sumando2)
dividendo = float(input("ingrese el dividendo:"))
divisor = float(input("ingrese divisor:"))
resultado = round(dividendo/divisor, 1)
#resultado = dividendo/divisor
print("resultado de la division", resultado)

frase = "holis\nme llamo adriana\ncomo estas?"
print(frase)

# ***** LISTAS *****
lista = ["ordenador", "teclado", "raton"]
print(lista)
lista = lista + ["mesa"]
print(lista)
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
listaoriginal = ["ordenador", "teclado", "raton"]
listanueva = ["monitor", "impresora", "altavoces"]
listafinal = listaoriginal + listanueva
print(listafinal)
lista = ["ordenador", "teclado", "raton"]
print(lista)
lista[0] = "monitor"
lista[1] = "impresora"
lista[2] = "altavoces"
del lista[1]
print(lista)
lista = ["ordenador", "teclado", "raton", ["tarjeta de sonido", "microfono", "altavoces"]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[3][2])

#***** TUPLAS *****
tupla = ("ordenador", "teclado", "raton")
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])


# ***** BOOLEANOS Y OPERADORES LOGICOS *****
variablebooleana = False
print(variablebooleana)
booleano1 = True
booleano2 = True
print(booleano1 or booleano2)
numero1 = 6
numero2 = 9
print(numero1 > numero2)
print(numero1 >= numero2)
print(numero1 < numero2)
print(numero1 <= numero2)
print(numero1 == numero2)
print(numero1 != numero2)
cadenaejemplo = "en un lugar de la mancha..."
print(cadenaejemplo.capitalize())
cadenaejemplo = "en un lugar de la mancha..."
print(cadenaejemplo.upper())
cadenaejemplo = "EN UN LUGAR DE LA MANCHA..."
print(cadenaejemplo.lower())
cadenaejemplo = "En un lugar de la mancha..."
print(len(cadenaejemplo))
cadenaejemplo = "En un lugar de la mancha..."
print(cadenaejemplo.isalnum())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalnum())

# ***** OPERADORES DE COMPARACION *****
numero = int(input("Escriba un numero del 1 al 10:"))
if numero > 10:
    print("¡El numero que has escrito es mayor que 10!")
print("Has escrito el numero" + str(numero))
cadenaejemplo = "En un lugar de la mancha..."
# if "niugar" in cadenaejemplo:
#     print("encontrado")
# else:
#     print("no encontrado")
if cadenaejemplo.startswith('e'):
    print("empieza por e")
else:
    print("no empieza por e")
if cadenaejemplo.endswith('p'):
    print("termina por p")
else:
    print("no termina por p")
numero1 = int(input("Escriba el primer numero:"))
numero2 = int(input("Escriba el segundo numero:"))
if numero1>numero2:
    print("el primer numero es mayor que el segundo")
elif numero1==numero2:
    print("Ambos numeros son iguales")
else:
    print("El primer numero es menor que el segundo")
i = 0
while i<10:
    print(i,end=" ")
    i = i + 1
continuar = True
while continuar:
    valor = int(input("ingrese un numero superior a 100:"))
    if valor>100:
        continuar=False
print("programa acabado")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in lista:
    print(item, end=" ")
for item in range(10):
   print(item, end=" ")
for item1 in range(3):
    for item2 in range(5):
        print("item1 =" + str(item1) + ", item2 =" + str(item2))
item1 = 0
while item1 < 3:
    for item2 in range(5):
        print("item1 =" + str(item1) + ",item2 =" + str(item2))
    item1 = item1 + 1
item1 = 0
while item1 <3:
    item2 = 0
    while item2<5:
        print("item1 = " + str(item1) + ",item2 = " + str(item2))
        item2 = item2 + 1
    item1 = item1 + 1

# ***** CALCULAORA INICIAL *****
fin = False
print("""***********
Calculadora
***********
Menu
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Salir""""")
while not fin:
    opc = int(input("Opcion:"))
    if opc == 1:
        sum1 = int(input("Sumando uno:"))
        sum2 = int(input("Sumando dos:"))
        print("La suma es:", sum1 + sum2)
    elif opc == 2:
        minuendo = int(input("minuendo:"))
        sustraendo = int(input("sustraendo:"))
        print("la resta es:", minuendo - sustraendo)
    elif opc == 3:
        multiplicando = int(input("multiplicando:"))
        multiplicador = int(input("multiplicador:"))
        print("la multiplicacion es:", multiplicando*multiplicador)
    elif opc == 4:
        dividendo = int(input("dividendo:"))
        divisor = int(input("divisor:"))
        print("la division es:", dividendo / divisor)
    elif opc == 5:
        fin = True

# ***** FUNCIONES *****
def Saludar():
   print("hola mundo")

Saludar()
def EsMayorQueCero(param):
    if param > 0:
        print(param, "es mayor que cero")
    elif param == 0:
        print(param, "es igual a cero")
    else:
        print(param, "es menor que cero")


numero = int(input("introduce un numero:"))
EsMayorQueCero(numero)

# ***** CLASES *****
class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y, ")")


p1 = Punto(4, 6)
p1.MostrarPunto()
class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y, ")")


p1 = Punto(4, 6)
p1.MostrarPunto()
p1.X = 7
p1.MostrarPunto()
class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y, ")")


p1 = Punto(4, 6)
p1.MostrarPunto()
p2 = Punto(3, 8)
p2.MostrarPunto()
p1 = p2
p1.MostrarPunto()
class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y, ")")


class Triangulo:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3

    def MostrarVertices(self):
        self.V1.MostrarPunto()
        self.V2.MostrarPunto()
        self.V3.MostrarPunto()


v1 = Punto(3, 4)
v2 = Punto(6, 8)
v3 = Punto(9, 2)
triangulo = Triangulo(v1, v2, v3)
triangulo.MostrarVertices()
