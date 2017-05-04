from datetime import date
class Personas(object):
    Nombre=""
    Apellido=""
    FechaN=None

    def setNombre (self, nombre):
        self.Nombre=nombre

    def setApellido (self, apellido):
        self.Apellido=apellido

    def setFecha (self, dia, mes, anio)
        self.Fecha= date(int(dia), int(mes), int(anio))

