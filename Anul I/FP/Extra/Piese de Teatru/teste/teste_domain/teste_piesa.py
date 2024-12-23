import unittest

from domain.piesa import Piesa
from domain.validator import PiesaValidator, ValidationException

class TestDomain(unittest.TestCase):
    def test_piesa(self):
        piesa = Piesa("titlu", "regizor", "Comedie", 10)
        self.assertEqual(piesa.get_titlu(), "titlu")
        self.assertEqual(piesa.get_regizor(), "regizor")
        self.assertEqual(piesa.get_gen(), "Comedie")
        self.assertEqual(piesa.get_durata(), 10)
        piesa.set_gen("Altele")
        self.assertEqual(piesa.get_gen(), "Altele")
        piesa.set_durata(20)
        self.assertEqual(piesa.get_durata(), 20)

    def test_piesa_validator(self):
        piesa = Piesa("titlu", "regizor", "Comedie", 10)
        validator = PiesaValidator()
        validator.validate(piesa)
        piesa_invalida = Piesa("", "", "NuEComedie", -1)
        self.assertRaises(ValidationException, validator.validate, piesa_invalida)

if __name__ == "__main__":
    unittest.main()
