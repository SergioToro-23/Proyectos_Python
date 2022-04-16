# funcion tipo generador---> el asterisco es que recibirta en forma de tupla varios elementos
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento
        #for subelemento in elemento:
        #yield subelemento

        #aqui accede a los sub elementos
        #yield from elemento    
        
# main
ciudades_devueltas = devuelve_ciudades("madrid","bogota","tokyo","rio")        

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))