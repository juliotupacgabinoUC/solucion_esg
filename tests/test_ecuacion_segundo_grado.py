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

    def test_solucionESG_parametrosNumericos_raicesReales_subTest(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43,
             "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00,
             "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.00,
             "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.24,
             "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.00,
             "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.00,
             "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.00,
             "RaizEsperada2": -2.00},
        )
        # Do
        for item in items:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado.a = item["a"]
                ecuacionSegundoGrado.b = item["b"]
                ecuacionSegundoGrado.c = item["c"]
            RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()
            # Assert
            self.assertAlmostEqual(item["RaizEsperada1"], RaizActual1, 2)
            self.assertAlmostEqual(item["RaizEsperada2"], RaizActual2, 2)


    def test_solucionESG_parametrosNumericos_raicesComplejasConjugadas(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        ecuacionSegundoGrado.a = 1
        ecuacionSegundoGrado.b = 2
        ecuacionSegundoGrado.c = 3
        raiz_esperada1 = complex(-1, 1.41)
        raiz_esperada2 = complex(-1, -1.41)
        # Do
        raiz_actual1, raiz_actual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertAlmostEqual(raiz_esperada1.real, raiz_actual1.real, 2)
        self.assertAlmostEqual(raiz_esperada1.imag, raiz_actual1.imag, 2)
        self.assertAlmostEqual(raiz_esperada2.real, raiz_actual2.real, 2)
        self.assertAlmostEqual(raiz_esperada2.imag, raiz_actual2.imag, 2)

    def test_solucionESG_parametrosNumericos_raicesComplejasConjugadas_subTest(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        items = (
            {"Case": "Caso 01", "a": 1, "b": 1, "c": 1, "RaizEsperada1": complex(-0.50, 0.87),
                "RaizEsperada2": complex(-0.50, -0.87)},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 3, "RaizEsperada1": complex(-1.00, 1.41),
                "RaizEsperada2": complex(-1.00, -1.41)},
        )
        # Do
        for item in items:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado.a = item["a"]
                ecuacionSegundoGrado.b = item["b"]
                ecuacionSegundoGrado.c = item["c"]
                raiz_esperada1 = item["RaizEsperada1"]
                raiz_esperada2 = item["RaizEsperada2"]

            raiz_actual1, raiz_actual2 = ecuacionSegundoGrado.solucionESG()
            # Assert
            self.assertAlmostEqual(raiz_esperada1.real, raiz_actual1.real, 2)
            self.assertAlmostEqual(raiz_esperada1.imag, raiz_actual1.imag, 2)
            self.assertAlmostEqual(raiz_esperada2.real, raiz_actual2.real, 2)
            self.assertAlmostEqual(raiz_esperada2.imag, raiz_actual2.imag, 2)

    def test_solucionESG_parametrosNoNumericos_lanzaException(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        with self.assertRaises(ValueError):
            ecuacionSegundoGrado.a = "a"

    def test_solucionESG_parametrosNoNumericos_lanzaException_subTest(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        items = (
            {"Case": "Caso 01", "a": "a", "b": "b", "c": "c"},
            {"Case": "Caso 02", "a": "a", "b": 1, "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "aa", "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "3,1", "c": 1},
        )
        for item in items:
            with self.subTest(item["Case"]):
                with self.assertRaises(ValueError):
                    ecuacionSegundoGrado.a = item["a"]
                    ecuacionSegundoGrado.b = item["b"]
                    ecuacionSegundoGrado.c = item["c"]