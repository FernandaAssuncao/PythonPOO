from Diario import Diario
from rich import inspect

if __name__ == '__main__':
    p1 = Diario()
    p1.escrever('I love Hector, he is my gentleman.')
    p1.escrever('Heitor never makes me feel insecure.')
    p1.escrever('He treats me like a queen')
    p1.escrever('He loves me deeply.')
    p1.ler('Fernanda')
    inspect(p1, private=True)
