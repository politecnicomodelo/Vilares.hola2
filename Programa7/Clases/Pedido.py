class Pedido (object):
    FechaC=None
    Plato=None
    Persona=None
    FechaE=None
    Entregado=None
    idpedido=None

    def __init__(self,fecha=None, plato=None, persona=None, hora=None, entregado=None, pedido=None):
        self.setEntrega(entregado)
        self.setFechaC(fecha)
        self.setFechaE(hora)
        self.setPlato(plato)
        self.setPersona(persona)
        self.setIdpedido(pedido)

    def setFechaC(self, a):
        self.FechaC=a

    def setPlato(self, b):
        self.Plato=b

    def setPersona(self, c):
        self.Persona=c

    def setFechaE(self, d):
        self.FechaE=d

    def setEntrega(self, e):
        self.Entregado=e

    def setIdpedido(self, f):
        self.idpedido=f

    def setDescuento(self):
        return (self.Plato.Precio*((100- self.Persona.getDesc()))/100)
