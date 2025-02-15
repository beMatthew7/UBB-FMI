import unittest
import os
from domain.carte import Carte
from repository.repository_carti import RepositoryCarti, RepositoryCartiFile

class TestRepositoryCarti(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryCarti()
        self.carte1 = Carte(1, "Titlu1", "Descriere1", "Autor1", 5)
        self.carte2 = Carte(2, "Titlu2", "Descriere2", "Autor2", 3)

    def test_store_book(self):
        self.repo.store_book(self.carte1)
        self.assertEqual(len(self.repo.get_all_books()), 1)
        self.repo.store_book(self.carte2)
        self.assertEqual(len(self.repo.get_all_books()), 2)

        with self.assertRaises(ValueError):
            self.repo.store_book(self.carte1)  

    def test_find_book(self):
        self.repo.store_book(self.carte1)
        found_carte = self.repo.find_book(1)
        self.assertEqual(found_carte, self.carte1)
        self.assertIsNone(self.repo.find_book(3))  

    def test_update_book(self):
        self.repo.store_book(self.carte1)
        updated_carte = Carte(1, "Titlu Nou", "Descriere Noua", "Autor Nou", 10)
        self.repo.update_book(updated_carte)

        carte_in_repo = self.repo.find_book(1)
        self.assertEqual(carte_in_repo.get_titlu(), "Titlu Nou")
        self.assertEqual(carte_in_repo.get_nr_bucati(), 10)

        with self.assertRaises(ValueError):
            self.repo.update_book(self.carte2)  

    def test_delete_book(self):
        self.repo.store_book(self.carte1)
        self.repo.store_book(self.carte2)

        self.repo.delete_book(1)
        self.assertEqual(len(self.repo.get_all_books()), 1)
        self.assertIsNone(self.repo.find_book(1))

        with self.assertRaises(ValueError):
            self.repo.delete_book(3)  
class TestRepositoryCartiFile(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_repo_carti.txt"
        with open(self.test_file, "w") as f:
            f.write("1,Titlu1,Descriere1,Autor1,5\n")
            f.write("2,Titlu2,Descriere2,Autor2,3\n")

        self.repo_file = RepositoryCartiFile(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_from_file(self):
        all_books = self.repo_file.get_all_books()
        self.assertEqual(len(all_books), 2)

        self.assertEqual(all_books[0].get_titlu(), "Titlu1")
        self.assertEqual(all_books[1].get_autor(), "Autor2")

    def test_store_book(self):
        new_book = Carte(3, "Titlu3", "Descriere3", "Autor3", 7)
        self.repo_file.store_book(new_book)

        with open(self.test_file, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 3)



    def test_delete_book(self):
        self.repo_file.delete_book(1)

        with open(self.test_file, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)
        self.assertNotIn("1,Titlu1,Descriere1,Autor1,5\n", lines)

if __name__ == "__main__":
    unittest.main()
