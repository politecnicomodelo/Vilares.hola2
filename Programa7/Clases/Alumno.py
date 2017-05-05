from .Persona import Persona
class Alumno(Persona):
    Division=None

    def __init__(self, nombre=None, apellido=None, dni=None, division=None):
        self.setNombre(nombre)
        self.setApellido(apellido)
        self.setDni(dni)
        self.setDivision(division)

    def setDivision(self, division):
        self.Division=division
