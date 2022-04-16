# Herencia, clase padre vehiculos
class Vehiculos():
    
    #constructor
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    #setter
    def arrancar(self):
        self.enmarcha=True
    #setter
    def acelerar(self):
        self.acelera=True
    #setter
    def frenar(self):
        self.frena=True
    #getter
    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
         self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


#clase hijo, hereda propiedades vehiculos
class Furgoneta(Vehiculos):
    
    #sett y get
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgonteta está cargada"
        else:
            return "La furgoneta no está cargada"


#clase hijo, hereda propiedades vehiculos
class Moto(Vehiculos):
    hcaballito=""

    #setter
    def caballito(self):
        self.hcaballito="haciendo caballito"

    #Getter(se llama igual que el del padre)ya que se sobreescribe el metodo y se usa el del hijo
    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
         self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


#clase hijo, hereda propiedades vehiculos
class V_Electricos(Vehiculos):
    #tiene un constructor
    def __init__(self,marca, modelo):
        #llama al metodo de la case padre
        super().__init__(marca, modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


#herencia multiple, se hereda el constructor del primer parametro(el orden es importante), y tambien los metodos que tengan el mismo nombre
class BicicletaElectrica(V_Electricos,Vehiculos):
    # ejecuta con super el estado de el padre y luego sigue al print
    def estado(self):
        super().estado()
        print("bicicleta andando")


        

miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Loganoso")
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici=BicicletaElectrica("adidas","a10")
miBici.estado()


