"""*********************************
"""*      ENCAPSULAMIENTO          *
"""*********************************
class PuntoPublico:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class PuntoPrivado:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def GetX(self):
        return self.__X

    def GetY(self):
        return self.__Y

    def SetX(self, x):
        self.__X = x

    def SetY(self, y):
        self.__Y = y


publico = PuntoPublico(4, 6)
privado = PuntoPrivado(7, 3)
print("Valores punto publico:", publico.X, ",", publico.Y)
print("Valores punto privado:", privado.GetX(), ",", privado.GetY())
publico.X = 2
privado.SetX(9)
print("Valores punto publico:", publico.X, ",", publico.Y)
print("Valores punto privado:", privado.GetX(), ",", privado.GetY())
class OperarValores:
    def __init__(self, v1, v2):
        self.__V1 = v1
        self.__V2 = v2

    def __Sumar(self):
        return self.__V1 + self.__V2

    def __Restar(self):
        return self.__V1 - self.__V2

    def Operar(self):
        print("El resultado de la suma es:", self.__Sumar())
        print("El resultado de la resta es:", self.__Restar())


operarvalores = OperarValores(7, 3)
operarvalores.Operar()
print("El resultado de la sema es:", operarvalores.__Sumar())

"""*********************************
"""*          HERENCIA             *
"""*********************************

class Electrodomestico:
    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0

    def Encender(self):
        self.__Encendido = True

    def Apagar(self):
        self.__Encendido = False

    def Encendido(self):
        return self.__Encendido

    def SetTension(self, tension):
        self.__Tension = tension

    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0

    def SetRPM(self, rpm):
        self.__RPM = rpm

    def SetKilos(self, kilos):
        self.__Kilos = kilos

    def MostrarLavadora(self):
        print("##########")
        print("Lavadora:")
        print("\tRPM:", self.__RPM)
        print("\tKilos:", self.__Kilos)
        print("\tTension:", self.GetTension())
        if self.Encendido():
            print("\t¡Lavadora encendida!")
        else:
            print("\tLavadora no encendida.")
        print("##########")


lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(7)
lavadora.SetTension(220)
lavadora.Encender()
lavadora.Apagar()
lavadora.MostrarLavadora()


class Electrodomestico:
    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0

    def Encender(self):
        self.__Encendido = True

    def Apagar(self):
        self.__Encendido = False

    def Encendido(self):
        return self.__Encendido

    def SetTension(self, tension):
        self.__Tension = tension

    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0

    def SetRPM(self, rpm):
        self.__RPM = rpm

    def SetKilos(self, kilos):
        self.__Kilos = kilos

    def MostrarLavadora(self):
        print("##########")
        print("Lavadora:")
        print("\tRPM:", self.__RPM)
        print("\tKilos:", self.__Kilos)
        print("\tTension:", self.GetTension())
        if self.Encendido():
            print("\t¡Lavadora encendida!")
        else:
            print("\tLavadora no encendida.")
        print("##########")


class Microondas(Electrodomestico):
    def __init__(self):
        self.__PotenciaMaxima = 0
        self.__Grill = False

    def SetPotenciaMaxima(self, potencia):
        self.__PotenciaMaxima = potencia

    def SetGrill(self, grill):
        self.__Grill = grill

    def MostrarMicroondas(self):
        print("######")
        print("Microondas.")
        print("\tPotenciaMaxima:", self.__PotenciaMaxima)
        if self.__Grill == True:
            print("\tGrill: Si")
        else:
            print("\tGrill: No")
        print("\tTension:", self.GetTension())
        if self.Encendido():
            print("\t¡Microondas encendida!")
        else:
            print("\tMicroondas no encendida.")
        print("######")


lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(7)
lavadora.SetTension(220)
lavadora.Encender()
microondas = Microondas()
microondas.SetPotenciaMaxima(800)
microondas.SetGrill(True)
microondas.SetTension(220)
microondas.Apagar()
lavadora.MostrarLavadora()
microondas.MostrarMicroondas()

class Hotel:
    def __init__(self):
        self.__NumeroHabitaciones = 0
        self.__Estrellas = 0

    def SetNumeroHabitaciones(self, habs):
        self.__NumeroHabitaciones = habs

    def SetEstrellas(self, estrellas):
        self.__Estrellas = estrellas

    def MostrarHotel(self):
        print("------")
        print("Hotel:")
        print("\tEstrellas:", self.__Estrellas)
        print("\tNumero de Habitaciones:", self.__NumeroHabitaciones)
        print("------")


class Restaurante():
    def __init__(self):
        self.__Tenedores = 0
        self.__HoraApertura = 0

    def SetTenedores(self, tenedores):
        self.__Tenedores = tenedores

    def SetHoraApertura(self, hora):
        self.__HoraApertura = hora

    def MostrarRestaurante(self):
        print("------")
        print("Restaurante:")
        print("\tTenedores:", self.__Tenedores)
        print("\tHora de Apertura:", self.__HoraApertura)
        print("------")


class Negocio(Hotel, Restaurante):
    def __init__(self):
        self.__Nombre = ""
        self.__Direccion = ""
        self.__Telefono = 0

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetDireccion(self, direccion):
        self.__Direccion = direccion

    def SetTelefono(self, telefono):
        self.__Telefono = telefono

    def MostrarNegocio(self):
        print("######")
        print("Negocio:")
        print("\tNombre:", self.__Nombre)
        print("\tDireccion:", self.__Direccion)
        print("\tTelefono:", self.__Telefono)
        self.MostrarHotel()
        self.MostrarRestaurante()
        print("######")


negocio = Negocio()
negocio.SetEstrellas(4)
negocio.SetNumeroHabitaciones(255)
negocio.SetTenedores(3)
negocio.SetHoraApertura(8)
negocio.SetNombre("Time of software")
negocio.SetDireccion("Calle Falsa 123")
negocio.SetTelefono(4545641654)
negocio.MostrarNegocio()
