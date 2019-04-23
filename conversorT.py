#termometro

class Termometro():
    def __init__(self):
        self.__unidadM = 'c'
        self.__temperatura = 0
    
    def __conversor(self,temperatura,unidad):
        if unidad =='c':
            return "{}ºF".format(temperatura*9/5+32)
        elif unidad == 'F':
            return "{}ºC".format((temperatura-32)+5/9)
        else:
            return "unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.temperatura,self.unidad)
    
    def unidadMedida(self,uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
    
    def temp(self,temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
    
    def mide (self,uniM = None):
        if uniM == None or uniM == self.unidadM:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.conversor(self.__temperatura,uniM)
            else:
                return self.__str__()
                
        
        
    
    