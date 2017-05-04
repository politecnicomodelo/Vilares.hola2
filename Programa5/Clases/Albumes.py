class Albumes(object):
    Titulo=""
    ListaCanciones=[]

    def setTituloAl(self, titulo):
        self.Titulo= titulo

    def AgregarCancion(self, cancion):
        self.ListaCanciones.append(cancion)