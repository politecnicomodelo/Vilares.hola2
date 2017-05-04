from Clases.Alumno import Alumno
from datetime import date
from Clases.Materias import Materias

a= Alumno()

a.setNombre("pirpipi")

a.setApellido("chuman")

a.setFecha(2017, 3, 17)

a.addNota(5)

a.addNota(9)

print(a.promedio())

mate = Materias()

mate.setMateria("Matematica")
mate.agregarNota(6)

a.listamaterias = mate

