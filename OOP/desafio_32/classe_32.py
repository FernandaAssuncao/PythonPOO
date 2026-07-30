class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError('O valor deve ser um numero')
        if valor < 0:
            raise ValueError('O valor da base deve ser maior que 0')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError('O valor deve ser um numero')
        if valor < 0:
            raise ValueError('O valor deve ser maior que 0')
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Você não pode definir a area desse jeito!!')

    @property
    def medidas(self):
        return f'Base: {self.base}\nAltura: {self.altura}\nArea: {self.area}'

    @medidas.setter
    def medidas(self, valorores:tuple):
        if not isinstance(valorores, tuple):
            raise TypeError('O valores devem ser informados dentro de uma tupla')
        if len(valorores) != 2:
            raise SyntaxError('Informe uma tupla com somente dois valores!')
        if isinstance(valorores[0], int) or isinstance(valorores[0], float):
            self.base = valorores[0]
        if isinstance(valorores[1], int) or isinstance(valorores[1], float):
            self.altura = valorores[1]

