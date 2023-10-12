class Persona():
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
     return self._nombre
    def set_nombre(self,new_nombre):
      self._nombre = new_nombre
 
michael = Persona("Michael",23)        
nombre = michael.get_nombre()
print(nombre)

michael.set_nombre("Mike")
nombre = michael.get_nombre()
print(nombre)