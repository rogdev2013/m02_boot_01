#map, filter,reduce

from functools import reduce

lista=[1,3,-1,15,9]

listaDobles = map(lambda x:x*2,lista)
print(list(listaDobles))

listaPares = filter(lambda x: x%2==0, lista)
print(list(listaPares))

sumatorio = reduce(lambda x,y: x+y,lista)
print(sumatorio)

suma100 = reduce(lambda x,y: x+y,range(101))
print(suma100)