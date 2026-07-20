from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = random.choice(self.golpes)
            print(f'[red]{self.nome}[/] atacou [green]{alvo.nome}[/] com [white]{golpe}[/]')
            alvo.receber_dado(forca)
        else:
            print(f'O ataque entre [yellow]{self.nome}[/] e [purple]{alvo.nome}[/] não pode acontecer!')

    def receber_dado(self, dano):
        fator = random.randint(1, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f'[red]{self.nome}[/] recebeu dano de [blue]{fator}[/]!')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['soco', 'chute', 'golpe de machado', 'pulo giratorio']

    def curar(self):
        fator = random.randint(1, 100)
        self.vida += fator
        print(f'[cyan]{self.nome}[/] enrolou uma atadura nos ferimentos e [magenta]recuperou {fator} pontos de vida![/]')



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Raio de luz', 'magia estatica', 'magia explosiva']

    def curar(self):
        fator = random.randint(1, 100)
        self.vida += fator
        print(f'[cyan]{self.nome}[/] fez uma magia de cura e [magenta]recuperou {fator} pontos de vida![/]')
