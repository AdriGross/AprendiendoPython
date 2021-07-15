# ***** CALCULADORA EVOLUTIVA *****
# -- CONTIENE MANEJO DE EXCEPCIONES
def LeerNumero(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Error: Tienes que ingresar un numero.")
        else:
            leido = True
    return numero


def Sumar():
    sum1 = LeerNumero("Sumando uno:")
    sum2 = LeerNumero("Sumando dos:")
    print("La suma es:", sum1 + sum2)


def Restar():
    minuendo = LeerNumero("minuendo:")
    sustraendo = LeerNumero("sustraendo:")
    print("la resta es:", minuendo - sustraendo)


def Multiplicar():
    multiplicando = LeerNumero("multiplicando:")
    multiplicador = LeerNumero("multiplicador:")
    print("la multiplicacion es:", multiplicando*multiplicador)


def Dividir():
    dividendo = LeerNumero("dividendo:")
    divisor = LeerNumero("divisor:")
    try:
        resultado = dividendo/divisor
    except ZeroDivisionError:
        print("¡ERROR: No puedes dividir por cero!")
    else:
        print("La division en:", resultado)


def MostrarMenu():
    print("""***********
Calculadora
***********
Menu
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Mostrar menu
6)Salir""""")


def Calculadora():
    fin = False
    MostrarMenu()
    while not(fin):
        opc = int(input("Opcion:"))
        if(opc == 1):
            Sumar()
        elif(opc == 2):
            Restar()
        elif(opc == 3):
            Multiplicar()
        elif(opc == 4):
            Dividir()
        elif(opc == 5):
            MostrarMenu()
        elif(opc == 6):
            fin = 1


Calculadora()