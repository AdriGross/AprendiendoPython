# ***** SISTEMA DE BIBLIOTECA *****

# *---- CLASE AUTOR ----*
class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def MostrarAutor(self):
        print("Autor: ", self.Nombre, "", self.Apellidos)


# *---- CLASE LIBRO ----*
class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn

    def AñadirAutor(self, autor):
        self.Autor = autor

    def MostrarLibro(self):
        print("-----Libro-----")
        print("Titulo:", self.Titulo)
        print("ISBN:", self.ISBN)
        self.Autor.MostrarAutor()
        print("-------------")

    def ObtenerTitulo(self):
        return self.Titulo


# *---- CLASE BIBLIOTEECA ----*
class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def NumeroLibros(self):
        return len(self.ListaLibros)

    def AñadirLibro(self, libro):
        self.ListaLibros = self.ListaLibros + [libro]

    def ListarLibros(self):
        print("####################################")
        for item in self.ListaLibros:
            item.MostrarLibro()
        print("#####################################")

    def BorrarLibro(self, titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionaborrar]
            print("¡Libro borrado correctamente!")
        else:
            print("¡Libro no encontrado!")

    def MostrarMenu(self):
        print("""Menu
        1) Añadir libro a la biblioteca
        2) Mostrar biblioteca
        3) Borrar libro
        4) ¿Numero de libros?
        5) Salir""")

    def AñadirLibroABiblioteca(biblioteca):
        titulo = input("Introduzca el titulo del libro:")
        isbn = input("Introduzca el ISBN del libro:")
        autornombre = input("Introduzca el nombre del autor:")
        autorapellidos = input("Introduzca el apellido del autor:")
        autor = Autor(autornombre, autorapellidos)
        libro = Libro(titulo, isbn)
        libro.AñadirAutor(autor)
        biblioteca.AñadirLibro(libro)
        return biblioteca

    def BorraLibro(self):
        titulo = input("Introduzca el titulo del libro a borrar:")
        self.BorrarLibro(titulo)

    def NumLibros(biblioteca):
        print("El numero de libros en la biblioteca es:", biblioteca.NumeroLibros())


# *---- PROGRAMA PRINCIPAL ----*
fin = False
biblioteca = Biblioteca()

while not fin:
    biblioteca.MostrarMenu()
    opcion = int(input("Seleccione opcion:"))
    if(opcion == 1):
        biblioteca.AñadirLibroABiblioteca()
    elif(opcion == 2):
        biblioteca.ListarLibros()
    elif(opcion == 3):
        biblioteca.BorraLibro()
    elif(opcion == 4):
        biblioteca.NumLibros()
    elif(opcion == 5):
        fin = True

print("Adios!")