# @ decoradores, setters & getters
class Persona():
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    @property   
    def nombre(self):
     return self._nombre
    @nombre.setter
    def nombre(self,new_nombre):
      self._nombre = new_nombre
    @nombre.deleter
    def nombre(self):
        del self._nombre
            
michael = Persona("Michael",23)        
nombre = michael.get_nombre
print(nombre)