# --Agenda en Python
# --Permite administrar los contactos mediante un ABMC

# *---- CLASE DIRECCION ----*
class Direccion:
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""

    def GetCalle(self):
        return self.__Calle

    def GetPiso(self):
        return self.__Piso

    def GetCiudad(self):
        return self.__Ciudad

    def GetCodigoPostal(self):
        return self.__CodigoPostal

    def SetCalle(self, calle):
        self.__Calle = calle

    def SetPiso(self, piso):
        self.__Piso = piso

    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad

    def SetCodigoPostal(self, codigopostal):
        self.__CodigoPostal = codigopostal


# *---- CLASE PERSONA ----*
class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaNacimiento = ""

    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetFechaNacimiento(self):
        return self.__FechaNacimiento

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetFechaNacimiento(self, fechanacimiento):
        self.__FechaNacimiento = fechanacimiento


# *---- CLASE TELEFONO ----*
class Telefono:
    def __init__(self):
        self.__TelefonoMovil = ""
        self.__TelefonoFijo = ""
        self.__TelefonoTrabajo = ""

    def GetTelefonoMovil(self):
        return self.__TelefonoMovil

    def GetTelefonoFijo(self):
        return self.__TelefonoFijo

    def GetTelefonoTrabajo(self):
        return self.__TelefonoTrabajo

    def SetTelefonoMovil(self, telefonomovil):
        self.__TelefonoMovil = telefonomovil

    def SetTelefonoFijo(self, telefonofijo):
        self.__TelefonoFijo = telefonofijo

    def SetTelefonoTrabajo(self, telefonotrabajo):
        self.__TelefonoTrabajo = telefonotrabajo


# *---- CLASE CONTACTO ----*
class Contacto(Persona, Direccion, Telefono):
    def __init__(self):
        self.__Email = ""

    def GetEmail(self):
        return self.__Email

    def SetEmail(self, email):
        self.__Email = email

    def MostrarContacto(self):
        print("---- Contacto ----")
        print("Nombre:", self.GetNombre())
        print("Apellidos:", self.GetApellidos())
        print("Fecha de nacimiento:", self.GetFechaNacimiento())
        print("Telefono Movil:", self.GetTelefonoMovil())
        print("Telefono fijo:", self.GetTelefonoFijo())
        print("Telefono trabajo:", self.GetTelefonoTrabajo())
        print("Calle:", self.GetCalle())
        print("Piso:", self.GetPiso())
        print("Ciudad:", self.GetCiudad())
        print("Codigo postal:", self.GetCodigoPostal())
        print("Email:", self.__Email)
        print("----------")


# *---- CLASE AGENDA ----*
class Agenda:
    def __init__(self, path):
        self.__ListaContactos = []
        self.__Path = path

    def CargarContactos(self):
        try:
            fichero = open(self.__Path, "r")
        except:
            print("ERROR: No existe el fichero de la agenda")
        else:
            contactos = fichero.readlines()
            fichero.close()
            if len(contactos)>0:
                for contacto in contactos:
                    datos = contacto.split("#")
                    if len(datos) == 11:
                        nuevocontacto = Contacto()
                        nuevocontacto.SetNombre(datos[0])
                        nuevocontacto.SetApellidos(datos[1])
                        nuevocontacto.SetFechaNacimiento(datos[2])
                        nuevocontacto.SetTelefonoMovil(datos[3])
                        nuevocontacto.SetTelefonoFijo(datos[4])
                        nuevocontacto.SetTelefonoTrabajo(datos[5])
                        nuevocontacto.SetCalle(datos[6])
                        nuevocontacto.SetPiso(datos[7])
                        nuevocontacto.SetCiudad(datos[8])
                        nuevocontacto.SetCodigoPostal(datos[9])
                        nuevocontacto.SetEmail(datos[10])
                        self.__ListaContactos = self.__ListaContactos + [nuevocontacto]
                    print("INFO: Se han cargado un total de ", len(self.__ListaContactos), "contactos")

    def CrearNuevoContacto(self, nuevocontacto):
        self.__ListaContactos = self.__ListaContactos + [nuevocontacto]

    def GuardarContactos(self):
        try:
            fichero = open(self.__Path, "w")
        except:
            print("ERROR: No se puede guardar")
        else:
            for contacto in self.__ListaContactos:
                texto = contacto.GetNombre() + "\n"
                fichero.write(texto)
                texto = contacto.GetApellidos() + "\n"
                fichero.write(texto)
                texto = contacto.GetFechaNacimiento() + "\n"
                fichero.write(texto)
                texto = contacto.GetTelefonoMovil() + "\n"
                fichero.write(texto)
                texto = contacto.GetTelefonoFijo() + "\n"
                fichero.write(texto)
                texto = contacto.GetTelefonoTrabajo() + "\n"
                fichero.write(texto)
                texto = contacto.GetCalle() + "\n"
                fichero.write(texto)
                texto = contacto.GetPiso() + "\n"
                fichero.write(texto)
                texto = contacto.GetCiudad() + "\n"
                fichero.write(texto)
                texto = contacto.GetCodigoPostal() + "\n"
                fichero.write(texto)
                texto = contacto.GetEmail() + "\n"
                fichero.write(texto)
            fichero.close()

    def MostrarAgenda(self):
        print("###### AGENDA ######")
        print("Numero de contactos:", len(self.__ListaContactos))
        for contacto in self.__ListaContactos:
            contacto.MostrarContacto()
        print("#########################")

    def BuscarContactoPorNombre(self, nombre):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() == nombre:
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados

    def BuscarContactosPorTelefono(self, telefono):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTelefonoMovil() == telefono
                or contacto.GetTelefonoFijo() == telefono
                or contacto.GetTelefonoTrabajo() == telefono):
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados

    def BorrarContactoPorNombre(self, nombre):
        listafinal = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() != nombre:
                listafinal = listafinal + [contacto]
        print("Info:", len(self.__ListaContactos) - len(listafinal), "contactos han sido borrados")
        self.__ListaContactos = listafinal

    def BorrarContactoPorTelefono(self, telefono):
        listafinal = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTelefonoMovil() == telefono
                or contacto.GetTelefonoFijo() == telefono
                or contacto.GetTelefonoTrabajo() == telefono):
                listafinal = listafinal + [contacto]
        print("Info:", len(self.__ListaContactos) - len(listafinal), "contactos han sido borrados")
        self.__ListaContactos = listafinal

    def ObtenerOpcion(self):
        leido = False
        while not leido:
            try:
                numero = int(input("Opcion: "))
            except ValueError:
                print("Error: Tienes que introducir un numero")
            else:
                leido = True
        return numero

    def MostrarMenu(self):
        print("""Menu
        1) Mostrar contactos
        2) Buscar contactos
        3) Crear contacto nuevo
        4) Borrar contacto
        5) Guardar contactos
        6) Salir""")

    def BuscarContactos(agenda):
        print("""Buscar contactos:
    1) Nombre
    2) Telefono
    3) Volver""")
        finbuscar = False
        while not finbuscar:
            opcbuscar = agenda.ObtenerOpcion()
            if opcbuscar == 1:
                encontrados = agenda.BuscarContactoPorNombre(input((">Introduce el nombre a buscar:")))
                if len(encontrados)>0:
                    print("###### CONTACTOS ENCONTRADOS ######")
                    for item in encontrados:
                        item.MostrarContacto()
                    print("######################")
                else:
                    print("INFO: No se han encontrado contactos")
                finbuscar = True
            elif opcbuscar == 2:
                encontrados = agenda.BuscarContactosPorTelefono(input((">Introduce el telefono a buscar:")))
                if len(encontrados)>0:
                    print("###### CONTACTOS ENCONTRADOS ######")
                    for item in encontrados:
                        item.MostrarContacto()
                    print("######################")
                else:
                    print("INFO: No se han encontrado contactos")
                finbuscar = True
            elif opcbuscar == 3:
                finbuscar = True

    def ProcesoCrearContacto(agenda):
        nuevocontacto = Contacto()
        nuevocontacto.SetNombre(input((">Introduce el nombre del contacto:")))
        nuevocontacto.SetApellidos(input((">Introduce los apellidos del contacto:")))
        nuevocontacto.SetFechaNacimiento(input((">Introduce la fecha de nacimiento del contacto:")))
        nuevocontacto.SetTelefonoMovil(input((">Introduce el telefono movil del contacto:")))
        nuevocontacto.SetTelefonoFijo(input((">Introduce el telefono fijo del contacto:")))
        nuevocontacto.SetTelefonoTrabajo(input((">Introduce el telefono del trabajo del contacto:")))
        nuevocontacto.SetCalle(input((">Introduce la calle de la direccion del contacto:")))
        nuevocontacto.SetPiso(input((">Introduce el piso de la direccion del contacto:")))
        nuevocontacto.SetCiudad(input((">Introduce la ciudad del contacto:")))
        nuevocontacto.SetCodigoPostal(input((">Introduce el codigo postal del contacto:")))
        nuevocontacto.SetEmail(input((">Introduce el Email del contacto:")))
        agenda.CrearNuevoContacto(nuevocontacto)

    def BorrarContacto(agenda):
        print("""Buscar contactos a borrar por:
    1) Nombre
    2) Telefono
    3) Volver""")
        finbuscar = False
        while not finbuscar:
            opcbuscar = agenda.ObtenerOpcion()
            if opcbuscar == 1:
                agenda.BorrarContactoPorNombre(input((">Introduce el nombnre a borrar:")))
                finbuscar = True
            elif opcbuscar ==2:
                agenda.BorrarContactoPorTelefono(input((">Introduce el telefono a borrar:")))
                finbuscar = True
            elif opcbuscar == 3:
                finbuscar = True

    def Main(self):
        agenda.CargarContactos()
        fin = False
        while not(fin):
            agenda.MostrarMenu()
            opc = agenda.ObtenerOpcion()
            if (opc == 1):
                agenda.MostrarAgenda()
            elif (opc == 2):
                agenda.BuscarContactos()
            elif (opc == 3):
                agenda.ProcesoCrearContacto()
            elif (opc == 4):
                agenda.BorrarContacto()
            elif (opc == 5):
                agenda.GuardarContactos()
            elif (opc == 6):
                fin = 1


# *---- PROGRAMA PRINCIPAL ----*
agenda = Agenda("agenda.txt")
agenda.Main()