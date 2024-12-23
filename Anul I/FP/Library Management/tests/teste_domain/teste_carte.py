import unittest
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte

class TestCarte(unittest.TestCase):
    def setUp(self):
        self.carte = Carte(1, "Titlu Test", "O carte despre teste", "Autor Test", 5)

    def test_getters(self):
        self.assertEqual(self.carte.get_id_carte(), 1)
        self.assertEqual(self.carte.get_titlu(), "Titlu Test")
        self.assertEqual(self.carte.get_descriere(), "O carte despre teste")
        self.assertEqual(self.carte.get_autor(), "Autor Test")
        self.assertEqual(self.carte.get_nr_bucati(), 5)
        self.assertFalse(self.carte.get_rental())  

    def test_setters(self):
        self.carte.set_titlu("Titlu Nou")
        self.carte.set_descriere("Descriere Noua")
        self.carte.set_autor("Autor Nou")
        self.carte.set_nr_bucati(10)
        self.carte.set_rental(True)

        self.assertEqual(self.carte.get_titlu(), "Titlu Nou")
        self.assertEqual(self.carte.get_descriere(), "Descriere Noua")
        self.assertEqual(self.carte.get_autor(), "Autor Nou")
        self.assertEqual(self.carte.get_nr_bucati(), 10)
        self.assertTrue(self.carte.get_rental())


    def test_str(self):
        self.assertEqual(
            str(self.carte),
            "[1] Carte: Titlu = Titlu Test; Descriere = O carte despre teste; Autor = Autor Test; Bucati valabile = 5"
        )

class TestValidatorCarte(unittest.TestCase):
    def setUp(self):

        self.validator = ValidatorCarte()

    def test_titlu_invalid(self):

        carte = Carte(1, "A", "Descriere validă", "Autor Valid", 5)
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte)
        self.assertIn("Titlul cartii trebuie sa aiba cel putin un caracter.", str(context.exception))

    def test_descriere_invalida(self):

        carte = Carte(2, "Titlu Valid", "", "Autor Valid", 5)
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte)
        self.assertIn("Descriere cartii trebuie sa aiba cel putin un caracter.", str(context.exception))

    def test_autor_invalid(self):

        carte = Carte(3, "Titlu Valid", "Descriere validă", "A", 5)
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte)
        self.assertIn("Autorul cartii trebuie sa aiba cel putin un caracter.", str(context.exception))

    def test_mai_multe_erori(self):
        carte = Carte(4, "A", "", "A", 5)
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte)
        error_message = str(context.exception)
        self.assertIn("Titlul cartii trebuie sa aiba cel putin un caracter.", error_message)
        self.assertIn("Descriere cartii trebuie sa aiba cel putin un caracter.", error_message)
        self.assertIn("Autorul cartii trebuie sa aiba cel putin un caracter.", error_message)

    def test_carte_valida(self):

        carte = Carte(5, "Titlu Valid", "Descriere validă", "Autor Valid", 5)
        try:
            self.validator.validate(carte)  
        except ValueError:
            self.fail("Validatorul a ridicat o eroare pentru o carte validă!")


if __name__ == "__main__":
    unittest.main()
