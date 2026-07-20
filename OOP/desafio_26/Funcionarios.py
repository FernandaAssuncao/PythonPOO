from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1670
    inss = 7.5
    def __init__(self, nome=None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0


    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.sal_min
        mensagem = f'O salario de [green]{self.nome}[/]({self.__class__.__name__}) é de [red]R${self.salario:.2f}[/] e corresponde a [blue]R${base:.2f}[/] salarios minimos.'
        panel = Panel(mensagem, title='Analise de Salarios', width=50)
        print(panel)


class Horista(Funcionario):
    def __init__(self, nome, valor=7.77, qnt_horas=220):
        super().__init__(nome)
        self.valor_hora = valor
        self.horas_trabalhadas = qnt_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto=Funcionario.sal_min):
        super().__init__(nome)
        self.salrio_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salrio_bruto - (self.salario_bruto * Funcionario.inss / 100)
