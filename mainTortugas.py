#Modulo mainTortugas
import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30,-10,10,30)
    __colorTurtle = ('red','blue','green','orange')
    
    
    def __init__(self,width,heigth):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,heigth)
        self.__screen.bgcolor('lightgray')
        self.__starLine = -width/2 + 20
        self.__finishLine = width/2 -20
        
        self.__creacionCorredores()
    
    
    def __creacionCorredores(self):    
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
    
    def competir(self):
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1, 20)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
                
        
        
        
if __name__ == '__main__': #Consultar que significa esto
    circuito = Circuito(640,480)
    circuito.competir()
