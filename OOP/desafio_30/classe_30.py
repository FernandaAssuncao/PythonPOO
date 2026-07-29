from hashlib import sha256

class Credencial:
    def __init__(self):
        self._hash = None

    @property
    def senha(self):
        return self._hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self._hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha incorreto')

    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario in self._hash:
            print('Senha valida!')
            return True
        else:
            print('Senha invalida!')
            return False
