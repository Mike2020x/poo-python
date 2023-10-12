from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod 
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años y trabajo como {self.actividad}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)   
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)   
    def hacer_actividad(self):
        print(f"Estoy trabajando como: {self.actividad}")
        
pedro = Estudiante("Pedro",25,"Masculino","Estudiante") 

mike = Trabajador("Mike",26,"Masculino","Programador")

pedro.presentarse()
pedro.hacer_actividad()
mike.presentarse()
mike.hacer_actividad()

