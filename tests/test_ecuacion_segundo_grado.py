import unittest
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado


class TestEcuacionSegundoGrado(unittest.TestCase):
    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        ecuacionSegundoGrado.a = 3
        ecuacionSegundoGrado.b = -5
        ecuacionSegundoGrado.c = 1
        RaizEsperada1 = 1.43
        RaizEsperada2 = 0.23
        # Do
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()
        # Assert
        self.assertAlmostEqual(RaizEsperada1, RaizActual1, 2)
        self.assertAlmostEqual(RaizEsperada2, RaizActual2, 2)
