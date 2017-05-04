from datetime import date
class Empleado (object):
    Nombre=""
    Apellido=""
    Telefono=""
    Nacimiento=None
    Dias=[False,False,False,False,False]
    ListaAsistencia=[]

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setApellido(self, apellido):
        self.Apellido = apellido

    def setTelefono(self, telefono):
        self.Telefono = telefono

    def setNacimiento(self, m, d, a):
        self.Nacimiento = date(int(a), int(m), int(d))

    def setDias(self,lunes,martes,miercoles,jueves,viernes):
        if lunes == 1:
            self.ListaAsistencia[0]=True
        if martes == 1:
            self.ListaAsistencia[1]=True
        if miercoles == 1:
            self.ListaAsistencia[2]=True
        if jueves == 1:
            self.ListaAsistencia[3]=True
        if viernes == 1:
            self.ListaAsistencia[4]=True
