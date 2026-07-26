from rich import print

class Diario:
    def __init__(self, senha='Fernanda'):
        self.__senha = senha.strip()
        self.__mensagems = []

    def escrever(self, msg):
        self.__mensagems.append(msg.strip())

    def ler(self, senha):
        if senha.strip() == self.__senha:
            print('[green]ACESSO PERMITIDO![/]')
            for mensagem in self.__mensagems:
                print(f':swan: - {mensagem}')
        else:
            print('[red]Senha incorreta! ACESSO NEGADO![/]')

    @property
    def senha(self):
        raise PermissionError('Ninguem tem permissão de ver a senha!')
