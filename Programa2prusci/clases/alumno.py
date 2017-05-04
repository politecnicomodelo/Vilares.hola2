class Alumno (object):
    nombre=""
    apellido=""
    listaMaterias=[]

    def __init__ (self):
        self.listaMaterias=[]

    def set_nombre(self, nombre):
        self.nombre=nombre

    def set_apellido(self, apellido):
        self.apellido=apellido

    def agregar_materia(self, materia):
        self.listaMaterias.append(materia)

    def lista_promedios(self):
        lista = []
        for item in self.listaMaterias:
            lista.append(item.promedio())
        return lista

    def menor_promedio(self):
        lista=[]
        for item in self.listaMaterias:
            lista.append(item.promedio())
        return min(lista)

    def mayor_promedio(self):
        lista=[]
        for item in self.listaMaterias:
            lista.append(item.promedio())
        return max(lista)

    def promedio_general(self):
        if len(self.lista_promedios())==0:
            return 0
        return sum(self.lista_promedios())/len(self.lista_promedios())
