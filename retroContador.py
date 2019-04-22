def contAtras(e):
    print("{},".format(e),end="")
    if e>0:
        contAtras(e-1)
        
contAtras(10)

def sumatorio(n):
    return n + sumatorio(n-1)

sumatorio(4)