#Funciones lambda

from funciones1nivel import sumaTodos

print(sumaTodos(3,lambda x:x**3))

doble = lambda x:x*2 #mas claro hacerlo asi
triple = lambda x: x**3

print(sumaTodos(3,doble))
print(sumaTodos(3,triple))

