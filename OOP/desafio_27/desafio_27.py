from personagens import *

if __name__ == '__main__':
    p1 = Guerreiro('Heitor Cortês', 9000)
    p2 = Mago('Fernanda Assunção', 10000)
    p2.atacar(p1, 1000)
    p1.atacar(p2, 100)
    p1.curar()
    p2.curar()
