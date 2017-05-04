from clases.alumno import Alumno
from clases.materia import Materia

unAlumno=Alumno()
otroAlumno=Alumno()

unAlumno.set_apellido("Vilares")
unAlumno.set_nombre("Martin")

materia1=Materia()
materia1.set_nombre("Castellano")
unAlumno.agregar_materia(materia1)
materia1.agregar_nota(5)
materia1.agregar_nota(4)

materia2=Materia()
materia2.set_nombre("Laboratorio 1")
materia2.agregar_nota(5)
unAlumno.agregar_materia(materia2)

print(unAlumno.menor_promedio())


