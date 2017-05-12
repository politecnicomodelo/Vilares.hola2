from Clases.Profesor import Profesor
from Clases.Platillo import Plato
from Clases.Alumno import Alumno
from Clases.Pedido import Pedido
from datetime import date

ListaPersonas=[]
ListaPedidos=[]
ListaPlatos=[]
idpedido=1

def addAlumno ():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("Dni: ")
    division=input("Division: ")
    alumno1=Alumno(nombre, apellido, int(dni), division)
    ListaPersonas.append(alumno1)

def addProfesor ():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("Dni: ")
    descuento=input("Descuento: ")
    profesor1=Profesor(nombre, apellido, int(dni), int(descuento))
    ListaPersonas.append(profesor1)

def addPlatillo ():
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    platillo1=Plato(nombre, int(precio))
    ListaPlatos.append(platillo1)

def addPedido (idpedido):
    plato=None
    persona=None
    print("Ingrese fecha de creacion")
    anio = input("Anio: ")
    mes = input("Mes: ")
    dia = input("Dia: ")
    FechaC=date(int(anio), int(mes), int(dia))
    while(True):
        nombre = input("Plato: ")
        A=None
        for item in ListaPlatos:
            if item.Nombre == nombre:
                plato=item
                A=1
                break
        if A==1:
            break
        print("Plato inexistente, ingrese de nuevo")
    while(True):
        dni = input("Persona (dni): ")
        A=None
        for item in ListaPersonas:
            if item.Dni == int(dni):
                persona=item
                A=1
                break
        if A==1:
            break
        print("Persona inexistente, ingrese de nuevo")
    print("Ingrese fecha de entrega")
    anio = input("Anio: ")
    mes = input("Mes: ")
    dia = input("Dia: ")
    FechaE=date(int(anio), int(mes), int(dia))
    entregado=input("Ya se entrego?: ")
    idpedido += 1
    pedido1=Pedido(FechaC, plato, persona, FechaE, entregado, idpedido)
    ListaPedidos.append(pedido1)

def modAlumno ():
    while(True):
        dni = input("Dni del alumno a modificar: ")
        A=None
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Alumno:
                    print("Alumno encontrado, modifique")
                    item.Nombre = input("Nombre: ")
                    item.Apellido = input("Apellido: ")
                    item.Dni = input("Dni: ")
                    item.Division = input("Division: ")
                    A=1
                    break
        if A==1:
            break
        print("Dni inexistente, ingrese de nuevo")

def modProfesor():
    while(True):
        dni = input("Dni del profesor a modificar: ")
        A=None
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Profesor:
                    print("Profesor encontrado, modifique")
                    item.Nombre = input("Nombre: ")
                    item.Apellido = input("Apellido: ")
                    item.Dni = input("Dni: ")
                    item.Descuento = input("Descuento: ")
                    A=1
                    break
        if A==1:
            break
        print("Dni inexistente, ingrese de nuevo")

def modPlatillo():
    while(True):
        nombre = input("Nombre del plato a modificar: ")
        for item in ListaPlatos:
            if item.Nombre == nombre:
                while(True):
                    nombre=input()
                    variable=0
                    for hola in ListaPlatos:
                        if hola.Nombre != nombre:
                            variable += 1
                    if variable == len(ListaPlatos):
                        return
                    print("Nombre ya existente, ingrese de nuevo")
            item.Nombre=nombre
            item.Precio=input()
            return
        print("Plato inexistente, ingrese de nuevo")

def modPedido():
    while(True):
        idpedidox = input("Id del pedido a modificar: ")
        A=None
        for item in ListaPedidos:
            if item.idpedido == idpedidox:
                item.Entregado=input("Se entrego?: ")
                A=1
                break
        if A==1:
            break
        print("Pedido inexistente, ingrese de nuevo")


def eliminarAlumno():
    while(True):
        dni = input("Dni del alumno a eliminar: ")
        A=None
        for item in ListaPersonas:
            if item.Dni == int(dni):
                if type(item) is Alumno:
                    ListaPersonas.remove(item)
                    A=1
                    break
        if A==1:
            break
        print("Dni inexistente, ingrese de nuevo")

def eliminarProfesor():
    while(True):
        dni = input("Dni del profesor a eliminar: ")
        A=None
        for item in ListaPersonas:
            if item.Dni == int(dni):
                if type(item) is Profesor:
                    ListaPersonas.remove(item)
                    A=1
                    break
        if A==1:
            break
        print("Dni inexistente, ingrese de nuevo")

def eliminarPlatillo():
    while(True):
        nombre = input("Nombre del plato a eliminar: ")
        A=None
        for item in ListaPlatos:
            if item.Nombre == nombre:
                ListaPlatos.remove(item)
                A=1
                break
        if A==1:
            break
        print("Plato inexistente, ingrese de nuevo")

def eliminarPedido():
    while(True):
        idpedidox = input("Id del pedido a eliminar: ")
        A=None
        for item in ListaPedidos:
            if item.idpedido == int(idpedidox):
                ListaPedidos.remove(item)
                A=1
                break
        if A==1:
            break
        print("Pedido inexistente, ingrese de nuevo")

def listadoPlatos():
    anio=input("Ingrese anio: ")
    mes=input("Mes: ")
    dia=input("Dia: ")
    fechaingr=date(int(anio), int(mes), int(dia))
    for item in ListaPedidos:
        if item.FechaE == fechaingr:
            print(item.Plato.Nombre + " " + item.Persona.Nombre + " " + item.Persona.Apellido + " " +
                   str(item.setDescuento()))

def textoAlumnos():
    f=open("ArchivoAlumnos.txt" ,"w")
    for item in ListaPersonas:
        if type(item) is Alumno:
            f.write(item.Nombre + " " + item.Apellido + " " + str(item.Dni) + " " + item.Division + '\n')
    f.close()

def textoProfesor():
    f=open("ArchivoProfesor.txt" ,"w")
    for item in ListaPersonas:
        if type(item) is Profesor:
            f.write(item.Nombre + " " + item.Apellido + " " + str(item.Dni) + " " + str(item.Descuento) + '\n')
    f.close()

def textoPlatos():
    f=open("ArchivoPlatos.txt" ,"w")
    for item in ListaPlatos:
        f.write(item.Nombre + " " + str(item.Precio) + '\n')
    f.close()

def textoPedidos():
    f=open("ArchivoPedidos.txt" ,"w")
    for item in ListaPedidos:
        f.write(str(item.idpedido) + " " + str(item.FechaC) + " " + str(item.FechaE) + " " + item.Entregado + " " + str(item.Persona.Dni)
                + " " + item.Plato.Nombre + '\n')
    f.close()

def cargarAlumnos():
    Aux=None
    p=open("ArchivoAlumnos.txt" ,"r")
    for line in p:
        if line == "":
            break
        Aux=line.split(" ")
        AlumnoAux=Alumno()
        AlumnoAux.setNombre(Aux[0])
        AlumnoAux.setApellido(Aux[1])
        AlumnoAux.setDni(int(Aux[2]))
        AlumnoAux.setDivision(Aux[3])
        ListaPersonas.append(AlumnoAux)
    p.close()

def cargarProfesor():
    Aux=None
    p=open("ArchivoProfesor.txt" ,"r")
    for line in p:
        if line == "":
            break
        Aux=line.split(" ")
        ProfesorAux=Profesor()
        ProfesorAux.setNombre(Aux[0])
        ProfesorAux.setApellido(Aux[1])
        ProfesorAux.setDni(int(Aux[2]))
        ProfesorAux.setDescuento(int(Aux[3]))
        ListaPersonas.append(ProfesorAux)
    p.close()

def cargarPlatos():
    Aux=None
    p=open("ArchivoPlatos.txt" ,"r")
    for line in p:
        if line == "":
            break
        Aux=line.split(" ")
        PlatoAux=Plato()
        PlatoAux.setNombre(Aux[0])
        PlatoAux.setPrecio(int(Aux[1]))
        ListaPlatos.append(PlatoAux)
    p.close()

def cargarPedidos():
    Aux=None
    p=open("ArchivoPedidos.txt" ,"r")
    for line in p:
        if line == "":
            break
        Aux=line.split(" ")
        PedidoAux=Pedido()
        PedidoAux.setIdpedido(Aux[0])
        fecha = Aux[1].split("-")
        PedidoAux.setFechaC(date(int(fecha[0]), int(fecha[1]), int(fecha[2])))
        fecha = Aux[2].split("-")
        PedidoAux.setFechaE(date(int(fecha[0]), int(fecha[1]), int(fecha[2])))
        PedidoAux.setEntrega(Aux[3])
        for item in ListaPersonas:
            if item.Dni == int(Aux[4]):
                PedidoAux.setPersona(item)
        for item in ListaPlatos:
            if item.Nombre == Aux[5][:-1]:
                PedidoAux.setPlato(item)
        ListaPedidos.append(PedidoAux)
    p.close()


while(True):

    print("1 - Agregar Alumno  2 - Agregar Profesor  3 - Agregar Plato  4 - Agregar Pedido")
    print("5 - Eliminar Alumno  6 - Eliminar Profesor  7 - Eliminar Plato  8 - Eliminar Pedido")
    print("9 - Mostrar Listado de Platos")
    print("10 - Modificar Alumno  11 - Modificar Profesor  12 - Modificar Plato  13 - Modificar Pedido")
    print("14 - Guardar Alumnos  15 - Guardar Profesores  16 - Guardar Platos  17 - Guardar Pedidos")
    print("18 - Cargar Alumnos  19 - Cargar Profesores  20 - Cargar Platos  21 - Cargar Pedidos")


    a=input()
    if int(a) == 1:
        addAlumno()
    if int(a) == 2:
        addProfesor()
    if int(a) == 3:
        addPlatillo()
    if int(a) == 4:
        addPedido(idpedido)
    if int(a) == 5:
        eliminarAlumno()
    if int(a) == 6:
        eliminarProfesor()
    if int(a) == 7:
        eliminarPlatillo()
    if int(a) == 8:
        eliminarPedido()
    if int(a) == 9:
        listadoPlatos()
    if int(a) == 10:
        modAlumno()
    if int(a) == 11:
        modProfesor()
    if int(a) == 12:
        modPlatillo()
    if int(a) == 13:
        modPedido()
    if int(a) == 14:
        textoAlumnos()
    if int(a) == 15:
        textoProfesor()
    if int(a) == 16:
        textoPlatos()
    if int(a) == 17:
        textoPedidos()
    if int(a) == 18:
        cargarAlumnos()
    if int(a) == 19:
        cargarProfesor()
    if int(a) == 20:
        cargarPlatos()
    if int(a) == 21:
        cargarPedidos()


























