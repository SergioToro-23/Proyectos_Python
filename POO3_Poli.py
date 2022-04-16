class Coche():

    def desplazamiento(self):
        print("Me despalazo en 4")

class Moto():

    def desplazamiento(self):
        print("Me desplazo en 2")

class Camion():
    def desplazamiento(self):
        print("Me desplazo en 6")
        
# esta es una forma:
# miVehiculo1=Coche()
# miVehiculo1.desplazamiento()  

# miVehiculo2=Moto()
# miVehiculo2.desplazamiento()

# miVehiculo3=Camion()
# miVehiculo3.desplazamiento()

#esta es otra
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Camion()
desplazamientoVehiculo(mivehiculo)
