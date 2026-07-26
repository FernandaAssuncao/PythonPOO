class Termostato:
    def __init__(self, temperatura=24.0):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if (temperatura >= 16) and (temperatura <= 30):
            if (temperatura * 10) % 5 == 0:
                self._temperatura = temperatura
            else:
                raise ValueError(f'A temperatura {temperatura} é invalida!')
        elif temperatura < 16:
            self._temperatura = 16.0
        elif temperatura > 30:
            self._temperatura = 30
