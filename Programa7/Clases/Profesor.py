from Persona import Persona
class Profesor(Persona):
    Descuento=None

    def setDescuento(self,descuento):
        self.Descuento=descuento

    def getDesc(self):
        return self.Descuento
