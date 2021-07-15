# ***** CALCULADORA *****
def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print("La suma es:", sum1 + sum2)


def Restar():
    minuendo = int(input("minuendo:"))
    sustraendo = int(input("sustraendo:"))
    print("la resta es:", minuendo - sustraendo)


def Multiplicar():
    multiplicando = int(input("multiplicando:"))
    multiplicador = int(input("multiplicador:"))
    print("la multiplicacion es:", multiplicando*multiplicador)


def Dividir():
    dividendo = int(input("dividendo:"))
    divisor = int(input("divisor:"))
    print("la division es:", dividendo / divisor)


def Calculadora():
    fin = False
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
            fin = 1


print("""***********
Calculadora
***********
Menu
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Salir""""")
Calculadora()