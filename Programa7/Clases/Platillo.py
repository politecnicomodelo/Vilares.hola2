class Plato (object):
    Nombre=None
    Precio=None

    def __init__(self, nombre=None, precio=None):
        self.setNombre(nombre)
        self.setPrecio(precio)

    def setNombre(self, nombre):
        self.Nombre=nombre

    def setPrecio(self, precio):
        self.Precio=precio

