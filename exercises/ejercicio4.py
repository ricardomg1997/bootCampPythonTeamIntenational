class Auto:
    marca = ""
    modelo = ""
    año = ""
    velocidad = 0
    frenar = ""

    def __init__(self, marca, modelo, año, frenar):
        # Propiedades
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
        self.frenar = frenar
    
    def acelerar(self):
            print(f"Soy un {self.marca}, estoy acelerando!!")

    def frenar_auto(self):
            print(f"Soy un {self.marca}, estoy frenando!!")
    
    def __str__(self):
        """Este método nos servirá para ver una representación en cadena del objeto"""
        return f"Auto(marca={self.marca}, modelo={self.modelo}, año={self.año}, velovidad={self.velocidad}, frenar={self.frenar})"
    
class AutoElectrico(Auto):

    def __init__(self, marca, modelo, año, frenar, autonomia, bateria):
         Auto.__init__(self, marca, modelo, año, frenar)
         self.autonomia = autonomia
         self.bateria = bateria

    def cargar_bateria(self):
        
        while self.bateria < 100:
            print(f"Cargando, nivel batería {self.bateria}")
            self.bateria += 10
        print(f"Cargado, nivel batería {self.bateria}")


obj_mazda = Auto('Mazda', 'Sedan', '2020', True)
carroElec = AutoElectrico("tesla", "v1", "2022", True, 30, 30)
carroElec.cargar_bateria()

