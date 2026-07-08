from rich import print

class Caneta:
    def __init__(self, cor='azul'):
        self.cor = cor.strip().lower()
        self.situacao = False
        self.__definir()

    def destampar(self):
        self.situacao = True

    def __definir(self):
        if self.cor == 'vermelho':
            self.cor = 'red'
        elif self.cor == 'azul':
            self.cor = 'blue'
        elif self.cor == 'amarelo':
            self.cor = 'yellow'
        elif self.cor == 'verde':
            self.cor = 'green'

    def escrever(self, mensagem):
        if self.situacao:
            print(f'[{self.cor}]{mensagem}[/]', end=' ')
        else:
            print('A caneta está tampada, destampe ela primeiro.')

    def quebrar_linha(self, quantidade):
        for c in range(1, quantidade + 1):
            print('\n')

c1 = Caneta('verde')
c2 = Caneta('vermelho')
c1.destampar()
c2.destampar()
c1.escrever('Oi')
c1.quebrar_linha(1)
c2.escrever('Tudo bem heitor? estou sentindo sua falta hoje, voce esta muito ocupado')
c3 = Caneta()
c3.destampar()
c3.quebrar_linha(1)
c3.escrever('Quando voce chegar do trabalho vou estar te esperando pra fazer a massagem que voce pediu, Eu te amo!')