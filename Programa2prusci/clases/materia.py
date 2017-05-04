class Materia(object):
    nombre=""
    listaNotas=[]

    def __init__(self):
        self.listaNotas=[]

    def set_nombre(self, n):
        self.nombre=n

    def agregar_nota(self, nota):
        self.listaNotas.append(nota)

    def promedio(self):
        if len(self.listaNotas)==0:
            return 0
        return sum(self.listaNotas)/len(self.listaNotas)
