#funcion generadora
def generaPares(limite):
    num=1
    
    while num<limite:
        yield num*2
        num+=1
    
devulevePares = generaPares(10)

print(next(devulevePares))
