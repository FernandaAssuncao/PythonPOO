from classe_31 import ContaBancaria

if __name__ == '__main__':
    cc = ContaBancaria(245, 'Heitor Cortês', 34000, 'fernandaminhadama')
    cc.sacar(600)
    cc.nome = 'Heitor Cortês Ferraz'
    cc.status_conta()
