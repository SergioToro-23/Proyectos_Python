import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError("el numero no puede ser negativo")
        #raise mipropioerror("eror chiuvis")
    else:
        return math.sqrt(num1)

op1 = (int(input("Introduce un número: ")))   
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")    