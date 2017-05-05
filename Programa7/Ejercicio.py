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
    alumno1=Alumno(nombre, apellido, dni, division)
    ListaPersonas.append(alumno1)

def addProfesor ():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("Dni: ")
    descuento=input("Descuento: ")
    profesor1=Profesor(nombre, apellido, dni, descuento)
    ListaPersonas.append(profesor1)

def addPlatillo ():
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    platillo1=Plato(nombre, precio)
    ListaPLatos.append(platillo1)

def addPedido (idpedido):
    plato=None
    persona=None
    print("Ingrese fecha de creacion")
    anio = input("Anio: ")
    mes = input("Mes: ")
    dia = input("Dia: ")
    FechaC=date(anio, mes, dia)
    while(True):
        plato = input("Plato: ")
        for item in ListaPlatos:
            if item.Plato == plato:
                break
        print("Plato inexistente, ingrese de nuevo")
    while(True):
        persona = input("Persona (dni): ")
        for item in ListaPersonas:
            if item.Dni == persona:
                break
        print("Persona inexistente, ingrese de nuevo")
    print("Ingrese fecha de entrega")
    anio = input("Anio: ")
    mes = input("Mes: ")
    dia = input("Dia: ")
    FechaE=date(anio, mes, dia)
    entregado=input("Ya se entrego?: ")
    idpedido += 1
    pedido1=Pedido(FechaC, plato, persona, FechaE, entregado, idpedido)
    ListaPedidos.append(pedido1)

def modAlumno ():
    while(True):
        dni = input("Dni del alumno a modificar: ")
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Alumno:
                    print("Alumno encontrado, modifique")
                    item.Nombre = input("Nombre: ")
                    item.Apellido = input("Apellido: ")
                    item.Dni = input("Dni: ")
                    item.Division = input("Division: ")
                    return
        print("Dni inexistente, ingrese de nuevo")

def modProfesor():
    while(True):
        dni = input("Dni del profesor a modificar: ")
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Profesor:
                    print("Profesor encontrado, modifique")
                    item.Nombre = input("Nombre: ")
                    item.Apellido = input("Apellido: ")
                    item.Dni = input("Dni: ")
                    item.Descuento = input("Descuento: ")
                    return
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
        for item in ListaPedidos:
            if item.idpedido == idpedidox:
                item.Entregado=input("Se entrego?: ")
                return
        print("Pedido inexistente, ingrese de nuevo")


def eliminarAlumno():
    while(True):
        dni = input("Dni del alumno a eliminar: ")
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Alumno:
                    ListaPersonas.remove(item)
                    return
        print("Dni inexistente, ingrese de nuevo")

def eliminarProfesor():
    while(True):
        dni = input("Dni del profesor a eliminar: ")
        for item in ListaPersonas:
            if item.Dni == dni:
                if type(item) is Profesor:
                    ListaPersonas.remove(item)
                    return
        print("Dni inexistente, ingrese de nuevo")

def eliminarPlatillo():
    while(True):
        nombre = input("Nombre del plato a eliminar: ")
        for item in ListaPlatos:
            if item.Nombre == nombre:
                ListaPlatos.remove(item)
                return
        print("Plato inexistente, ingrese de nuevo")

def eliminarPedido():
    while(True):
        idpedidox = input("Id del pedido a modificar: ")
        for item in ListaPedidos:
            if item.idpedido == idpedidox:
                ListaPedidos.remove(item)
                return
        print("Pedido inexistente, ingrese de nuevo")

def listadoPlatos():
    anio=input("Ingrese anio: ")
    mes=input("Mes: ")
    dia=input("Dia: ")
    fechaingr=date(anio, mes, dia)
    for item in ListaPlatos:
        if item.FechaE == fechaingr:
            print (Pedido.Plato.Nombre + " " + Pedido.Persona.Nombre + " " + Pedido.Persona.Apellido + " " +
                   str(Pedido.Plato.Precio*Pedido.Plato.setDescuento))


while(True):

    print("1 - Agregar Alumno")
    print("2 - Agregar Profesor")
    print("3 - Agregar Plato")
    print("4 - Agregar Pedido")
    print("5 - Eliminar Alumno")
    print("6 - Eliminar Profesor")
    print("7 - Eliminar Plato")
    print("8 - Eliminar Pedido")
    print("9 - Mostrar Listado de Platos")
    print("A - Modificar Alumno")
    print("B - Modificar Profesor")
    print("C - Modificar Plato")
    print("D - Modificar Pedido")

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
    if a == "A":
        modAlumno()
    if a == "B":
        modProfesor()
    if a == "C":
        modPlatillo()
    if a == "D":
        modPedido()

























