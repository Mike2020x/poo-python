class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"    

def hacer_ruido(animal):
        print(animal.sonido())
        
gato = Gato()
perro = Perro()
        
hacer_ruido(perro)

print(gato.sonido())