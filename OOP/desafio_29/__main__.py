from Diario import Diario
from rich import inspect

if __name__ == '__main__':
    p1 = Diario()
    p1.escrever('O heitor é meu cavalheiro')
    p1.escrever('Ele me trata como uma rainha')
    p1.escrever('Ele me ama profundamente')
    p1.ler('Fernanda')
    inspect(p1, private=True)
