from poligonos import *
from rich import print, inspect

if __name__ == '__main__':
    p1 = Circulo(6)
    print(f'O poligono [red]{type(p1).__name__}[/] tem uma area de [green]{p1.area():.2f}[/]cm')
    print(f'O poligono [blue]{type(p1).__name__}[/] tem um perimetro de [red]{p1.perimetro():.2f}[/]cm')
    inspect(p1)
