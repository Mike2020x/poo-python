class Auto():
    def __init__(self):
        self._estado = "apagado"
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")
    def conducir(self):
       if self._estado == "apagado":
        self.encender()
        print("Conduciendo")
        
        
auto = Auto()

auto.conducir()