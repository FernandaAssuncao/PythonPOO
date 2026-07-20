from exercicios.ex10.ex10 import Avaliacao
from rich import print

if __name__ == '__main__':
    p1 = Avaliacao('Heitor Cortês', 'Financias', 9.5)
    p1.nota = 10
    print(f'O aluno {p1.nome} tirou {p1.nota} na disciplina {p1.disciplina}!')
