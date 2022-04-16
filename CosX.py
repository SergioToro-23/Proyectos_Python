

#x=int(input("ingrese valor a calcular coseno: "))
#x=x*3.1416/180
#r = 1 - (x*x)/2 + (x*x*x*x)/24 + (x*x*x*x*x*x)/720 
#print(r)

x=int(input("ingrese valor a calcular coseno: "))
x=x*3.1416/180
pow=x
uno=1
#for n 1 a 3
y=1
for n in range(1,14):
    f=n*2    
    factorial=1
    #para cada valor calcula el factorial par
    for j in range(1,f+1):
        factorial=factorial*j

    pow=x
    #para cada valor calcula el exponente   
    for k in range(1,f):
        pow=pow*x
        
    #print("potencia",pow)
    #print("factorial",factorial)    
    uno=uno*-1
    #print("el signo",uno) 
    y=y+((uno)*(pow)/(factorial))        
 
print(y)


