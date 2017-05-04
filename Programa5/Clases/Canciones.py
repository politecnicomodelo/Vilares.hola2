
class Canciones(object):
    Titulo=""
    ListaAutores=[]
    ListaArtistas=[]

    def setTitulo(self, titulo):
        self.Titulo = titulo

    def AgregarAutor(self, Roberto):
        self.ListaAutores.append(Roberto)

    def AgregarArtista(self, Luis):
        self.ListaArtistas.append(Luis)


