class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    def mover(self, distancia):
        if self.combustible >=distancia/2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("No hay combustible suficiente")    
    
    
class Tanque_de_combustible:
    def __init__(self):
                self.combustible = 100
