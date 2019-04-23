class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("No hay Perro")
            
        if self.peso>=8:
            print("GUAO,GUAO,GUAO")
        else:
            print("ay,ay")




class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso>=8:
            print("GUAO,GUAO,GUAO")
        else:
            print("ay,ay")
    
    def __str__(self):
        return "Perro{},edad:{},peso:{}".format(self.nombre,self.edad,self.peso)
    
class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = false
    
    def __str__(self):
        return "Perro de Asistencia de {}".format (self.amo)
    
    def ladrar(self):
        if self.trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            

    