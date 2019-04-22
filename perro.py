class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso>=8:
            print("GUAO,GUAO,GUAO")
        else:
            print("guao,guao")