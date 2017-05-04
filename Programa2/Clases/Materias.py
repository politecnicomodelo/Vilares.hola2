class Materias (object):

    nombre = ""

    notas = []

    def setMateria(self, n):
        self.nombre = str(n)

    def agregarNota(self, j):
        self.notas.append(j)

