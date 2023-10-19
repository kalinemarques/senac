class Triangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    def calculaArea(self):
        area = (self.__base * self.__altura) / 2
        return print(f'A área do triângulo é {area}')

class Circulo:
    def __init__(self, raio):
        self.__raio = raio
    def calculaArea(self):
        pi = 3.14
        area = pi*(self.__raio**2)
        return print(f'A área do circulo é {area}')

class Retangulo(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculaArea(self):
        area = (self._Triangulo__base * self._Triangulo__altura)
        return print(f'A área do retangulo é {area}')

class Paralelogramo(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculaArea(self):
        area = (self._Triangulo__base * self._Triangulo__altura)
        return print(f'A área do paraleloframo é {area}')

class Trapezio(Triangulo):
    def __init__(self, baseMaior, base, altura):
        super().__init__(base, altura)
        self.__baseMaior = baseMaior
    def calculaArea(self):
        area = ((self.__baseMaior - self._Triangulo__base) * self._Triangulo__altura) + (self._Triangulo__base * self._Triangulo__altura)
        return print(f'A área do trapézio é {area}')

class Losango(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculaArea(self):
        area = (self._Triangulo__base * self._Triangulo__altura) / 2
        return print(f'A área do losango é {area}')
    
teste = Trapezio(8, 3, 4)
teste.calculaArea()

teste = Losango(3, 4)
teste.calculaArea()

teste = Paralelogramo(10, 6)
teste.calculaArea()

teste = Retangulo(10, 6)
teste.calculaArea()

teste = Triangulo(8, 12)
teste.calculaArea()

teste = Circulo(12)
teste.calculaArea()