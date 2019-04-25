#Modulo mainTortugas
import turtle

class Circuito():
    corredores = []
    
    def __init__(self,width,heigth):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,heigth)
        self.__screen.bgcolor('lightgray')
        
if __name__ == '__main__': #Consultar que significa esto
    circuito = Circuito(640,480)
