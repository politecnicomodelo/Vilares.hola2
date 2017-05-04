from datetime import date

from .Materias import Materias


class Alumno(object):
    nombre = ""

    apellido = ""

    fecha = None

    m = Materias()

    listamaterias = []

    def setMateria(self, n):
        (self.materias).append(n)

    def setPromediox(self, ):

    def setNombre(self, n):
        self.nombre = str(n)

    def setApellido(self, t):
        self.apellido = str(t)

    def setFecha(self, a, b, c):
        self.fecha = date(int(a), int(b), int(c))

    def minNota(self):
        return min(self.listanotas)

    def maxNota(self):
        return max(self.listanotas)

    def promedio(self):
        return sum(self.listanotas) / len(self.listanotas)
