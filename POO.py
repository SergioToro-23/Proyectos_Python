class Coche():
    
    #Constructor
    def __init__(self):
        #variable encapsulada
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    #metodo
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()


        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "algo fue mal al checkear"
        else:
            return "El coche está parado"

    #metodo
    def estado(self):
        print("El coche tiene ", self.__ruedas,"ruedas. Un ancho de ", self.__anchoChasis, "y un largo de",self.__largoChasis)

    #metodo que solo se ejecuta dentro, encapsulado
    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

# main
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------------Ahora el segundo objeto--------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


