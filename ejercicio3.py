class Animal():
    def comer(self):
        print("comiendo")
        
        
class Mamifero(Animal):
    def amamantar(self):
        print("amamantando")
        
        
class Ave(Animal):
    def volar(self):
        print("volando")
        
        
class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()