class celular:
    def __init__(self, marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def   llamar(self):
        print(f"llamado desde un:{self.modelo}")
    def cortar(self):
        print(f"cortaste el llamado desde tu:{self.modelo}")  
             
celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","Iphone","96MP")

celular1.llamar()
celular1.cortar()
print(celular2.marca)



