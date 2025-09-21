import unittest
from calendar_exercise import MiCalendario, ValorIncorrecto

class TestMiCalendario(unittest.TestCase):

    def setUp(self):
        self.calendario = MiCalendario()

    def test_lunes_2023(self):
        # En 2023 hubo 52 lunes
        self.assertEqual(self.calendario.count_weekday_in_year(2023, 0), 52)

    def test_domingo_2024(self):
        # En 2024 hay 52 domingos
        self.assertEqual(self.calendario.count_weekday_in_year(2024, 6), 52)

    def test_valor_incorrecto(self):
        # Lanzará excepción si el número está fuera de rango
        with self.assertRaises(ValorIncorrecto):
            self.calendario.count_weekday_in_year(2024, 8)

if __name__ == '__main__':
    unittest.main()
