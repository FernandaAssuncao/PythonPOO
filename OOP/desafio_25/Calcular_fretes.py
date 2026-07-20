from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calcular_frete(self):
        return f'O valor do frete para {self.distancia}Km é R${self.distancia * self.fator}'

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calcular_frete(self):
        if self.distancia >= 50:
            return f'O valor do frete para {self.distancia}Km é R${self.distancia * self.fator}'
        else:
            return 'O valor minimo para o caminhao é de 50Km'

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calcular_frete(self):
        if self.distancia <= 10:
            return f'O valor do frete para {self.distancia}Km é R${self.distancia * self.fator}'
        else:
            return 'O valor maximo para o drone é de 10km'
