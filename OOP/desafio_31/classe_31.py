from hashlib import sha256

from pydantic_core.core_schema import none_schema
from rich import print
from rich.panel import Panel

class ContaBancaria:
    def __init__(self, id: int, nome: str, saldo: float = 0, chave: str = None):
        self._id = id
        self._titular = nome
        self._saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self._hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f'Conta {self._id} criada com sucesso! Saldo da conta R${self._saldo}')

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput('Senha: ')).strip()
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self, chave: str) -> bool:
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self._hash:
            return True
        else:
            return False

    def sacar(self, valor: float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self._saldo:
                print(f'O saldo da conta é de {self._saldo}. SALDO INSUFICIENTE')
            else:
                self._saldo -= valor
                print(f'Saque de R${valor} APROVADO na conta {self._id}')
        else:
            print('Senha não confere. saque negado!')

    def status_conta(self):
        mensagem = f'Saldo: {self._saldo}\nTitular: {self._titular}'
        caixa = Panel(mensagem, title='Status da conta', width=50)
        print(caixa)

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome: str):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = nome
        else:
            print('Senha não confere, não foi possivel alterar o nome!')

