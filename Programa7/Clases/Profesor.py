from Persona import Persona
class Profesor(Persona):
    Descuento=None

    def __init__(self, nombre=None, apellido=None, dni=None, descuento=None):
        self.setNombre(nombre)
        self.setApellido(apellido)
        self.setDni(dni)
        self.setDescuento(descuento)


    def setDescuento(self,descuento):
        self.Descuento=descuento

    def getDesc(self):
        return self.Descuento

