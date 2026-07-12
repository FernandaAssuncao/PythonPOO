from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        self.preparar()
        self.ferver_agua()
        pass

    def preparar(self):
         return 'A bebida está sendo preparada a 180°C'

    def ferver_agua(self):
        return 'A agua está fervida!'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'A agua foi misturada ao pó de cafe!!'

    def servir(self):
        print(self.ferver_agua())
        print(self.preparar())
        print(self.misturar())
        return 'O café foi servido bom apetite!'

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'O chache foi misturado a agua!!'

    def servir(self):
        print(self.ferver_agua())
        print(self.preparar())
        print(self.misturar())
        return 'O chá esta pronto, bom apetite!'

class Capputino(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'O leite foi misturado ao cafe!!'

    def servir(self):
        print(self.ferver_agua())
        print(self.preparar())
        print(self.misturar())
        return 'Seu capputino foi servido, bom apetite!!'
