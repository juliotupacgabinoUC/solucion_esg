import math
class EcuacionSegundoGrado:
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        """Getter para a"""
        return self._a

    @a.setter
    def a(self, valor):
        """Setter para a"""
        if isinstance(valor, (int, float)):
            self._a = valor
        else:
            raise ValueError("a debe ser un número")

    @property
    def b(self):
        """Getter para b"""
        return self._b

    @b.setter
    def b(self, valor):
        """Setter para b"""
        if isinstance(valor, (int, float)):
            self._b = valor
        else:
            raise ValueError("b debe ser un número")

    @property
    def c(self):
        """Getter para c"""
        return self._c

    @c.setter
    def c(self, valor):
        """Setter para c"""
        if isinstance(valor, (int, float)):
            self._c = valor
        else:
            raise ValueError("c debe ser un número")

    def solucionESG(self):
        return None, None


    def solucionESG(self):
        d = math.pow(self.b, 2) - 4 * self.a * self.c
        if d >= 0:
            r1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            return r1, r2

    def solucionESG(self):
        d = math.pow(self.b, 2) - 4 * self.a * self.c
        if d >= 0:
            r1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        else:
            parteReal = -self.b / (2 * self.a)
            parteImaginaria = math.sqrt(math.fabs(d)) / (2 * self.a)
            r1 = complex(parteReal, parteImaginaria)
            r2 = complex(parteReal, -parteImaginaria)
        return r1, r2