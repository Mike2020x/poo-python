class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
         print(f"{self.nombre} Esta estudiando")
        
        
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
grado = int(input("Ingrese su grado: "))

Estudiante1 = Estudiante(nombre,edad,grado)
print(f"""
      DATOS DEL ESTUDIANTE: \n\n 
      Nombre: {Estudiante1.nombre}\n
      Edad: {Estudiante1.edad}\n
      Grado: {Estudiante1.grado}\n
      \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        Estudiante1.estudiar()