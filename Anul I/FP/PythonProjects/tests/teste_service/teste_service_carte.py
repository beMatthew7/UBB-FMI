import unittest
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte
from repository.repository_carti import RepositoryCarti
from service.controller_carte import ControllerCarti


class TestControllerCarti(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryCarti()
        self.validator = ValidatorCarte()
        self.controller = ControllerCarti(self.repo, self.validator)

        self.controller.add_default()

    def test_adauga_carte(self):
        self.controller.adauga_carte(106, "Test Titlu", "Test Descriere", "Test Autor", 10)
        carti = self.controller.get_all_books()
        self.assertEqual(len(carti), 6)

        with self.assertRaises(ValueError):
            self.controller.adauga_carte(101, "Duplicate ID", "Descriere", "Autor", 5)



    def test_delete_carte(self):
        self.controller.delete_carte(101)
        carti = self.controller.get_all_books()
        self.assertEqual(len(carti), 4)
        with self.assertRaises(ValueError):
            self.controller.delete_carte(101)  

    def test_filtreaza_dupa_autor(self):
        rezultate = self.controller.filtreaza_dupa_autor("George Orwell")
        self.assertEqual(len(rezultate), 1)
        self.assertEqual(rezultate[0].get_titlu(), "1984")

        rezultate_goale = self.controller.filtreaza_dupa_autor("Autor Inexistent")
        self.assertEqual(len(rezultate_goale), 0)

    def test_cauta_carte_dupa_titlu(self):
        carte = self.controller.cauta_carte_dupa_titlu("Dune")
        self.assertIsNotNone(carte)
        self.assertEqual(carte.get_autor(), "Frank Herbert")

        carte_inexistenta = self.controller.cauta_carte_dupa_titlu("Inexistent")
        self.assertIsNone(carte_inexistenta)

    def test_cauta_carte_dupa_titlu_si_autor(self):
        carte = self.controller.cauta_carte_dupa_titlu_si_autor("1984", "George Orwell")
        self.assertIsNotNone(carte)

        carte_inexistenta = self.controller.cauta_carte_dupa_titlu_si_autor("1984", "Autor Inexistent")
        self.assertIsNone(carte_inexistenta)

    def test_genereaza_carti_random(self):
        initial_count = len(self.controller.get_all_books())
        self.controller.genereaza_carti_random(10)
        final_count = len(self.controller.get_all_books())
        self.assertEqual(final_count, initial_count + 10)


    def test_find_carte(self):
        carte = self.controller.find_carte(101)
        self.assertIsNotNone(carte)
        self.assertEqual(carte.get_titlu(), "Dune")

        carte_inexistenta = self.controller.find_carte(999)
        self.assertIsNone(carte_inexistenta)

    def test_get_all_books(self):
        carti = self.controller.get_all_books()
        self.assertEqual(len(carti), 5)  

if __name__ == "__main__":
    unittest.main()
