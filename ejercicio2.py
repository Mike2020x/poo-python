class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_saludo(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")
     
     
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def mostrar_grado(self):
        print(f"Estoy estudiando {self.grado}") 
         
         

student = Estudiante("Juan",20,3)

student.mostrar_saludo()
student.mostrar_grado()
