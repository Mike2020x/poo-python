# Crear un juego de fusiön.
# El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar
# para formar personajes mås poderosos que tengan mås poder...
# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
# se fusionen, salga un nuevo personaje con habilidades mejoradas.
# una posible formula es: el promedio de las habilidades de ambos al cuadrado

class Personaje():
    def __init__(self, nombre, fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __repr__(self):
        return f"{self.nombre} (fuerz:{self.fuerza},velocidad:{self.velocidad})"
    def __add__(self, otro):
        nuevo_nombre = self.nombre + "-" +otro.nombre
        nueva_fuerza = round(((self.fuerza + otro.fuerza)/2) ** 2)
        nueva_velocidad = round(((self.velocidad + otro.velocidad)/2) ** 2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
        
goku = Personaje("Goku", 100, 100)    
vegeta = Personaje("Vegeta", 90, 80)    

gogeta = goku + vegeta

print(gogeta)