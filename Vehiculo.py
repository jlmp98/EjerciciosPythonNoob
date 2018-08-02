class Vehiculo:

    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self,color, ruedas, velocidad, cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "{}Kms/h, {}Cc".format(self.velocidad, self.cilindrada)

c1 = Coche("Rojo",4,150,1000)

class Camioneta(Coche):

    def __init__(self,color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color,ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + "| Carga : {}".format(self.carga)

c2 = Camioneta("Rojo",4,150,1000,100)

class Bicicleta(Vehiculo):

    def __init__(self,color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + " | Tipo : {}".format(self.tipo)

bici = Bicicleta("Rojo",2,"Montaña")

class Motocicleta(Bicicleta):

    def __init__(self,color, ruedas,tipo, velocidad, cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "{}Kms/h, {}Cc".format(self.velocidad, self.cilindrada)


moto = Motocicleta("Rojo", 2,"Deportiva",150, 1000)

Taller = [c1,c2,bici,moto]

for x in Taller:
    print(type(x).__name__, x)
    if x.ruedas == 2:
        print("Se trata de una bicicleta o una moto")
    elif x.ruedas == 4:
        print("Se trata de un coche o camion")



