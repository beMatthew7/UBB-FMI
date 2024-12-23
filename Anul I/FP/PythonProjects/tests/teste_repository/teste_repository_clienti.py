import unittest
import os
from domain.client import Client
from repository.repository_clienti import RepositoryClientiFile, RepositoryClienti

class TestRepositoryClienti(unittest.TestCase):

    def setUp(self):
        self.repo = RepositoryClienti()

    def test_store_client(self):
        client = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client)
        self.assertEqual(len(self.repo.get_all_clients()), 1)

    def test_store_client_duplicate_id(self):
        client1 = Client(1, "Ion Popescu", "1234567890123")
        client2 = Client(1, "Maria Ionescu", "2345678901234")
        self.repo.store_client(client1)
        with self.assertRaises(ValueError):
            self.repo.store_client(client2)

    def test_find_client(self):
        client = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client)
        found_client = self.repo.find_client(1)
        self.assertEqual(found_client.get_nume(), "Ion Popescu")

    def test_find_client_not_found(self):
        client = self.repo.find_client(999)
        self.assertIsNone(client)

    def test_update_client(self):
        client = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client)
        updated_client = Client(1, "Ion Ionescu", "9876543210987")
        self.repo.update_client(updated_client)
        self.assertEqual(self.repo.find_client(1).get_nume(), "Ion Ionescu")

    def test_delete_client(self):
        client = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client)
        self.repo.delete_client(1)
        self.assertEqual(len(self.repo.get_all_clients()), 0)

    def test_delete_client_not_found(self):
        with self.assertRaises(ValueError):
            self.repo.delete_client(999)

    def test_get_size(self):
        client1 = Client(1, "Ion Popescu", "1234567890123")
        client2 = Client(2, "Maria Ionescu", "2345678901234")
        self.repo.store_client(client1)
        self.repo.store_client(client2)
        self.assertEqual(self.repo.get_size(), 2)

class TestRepositoryClientiFile(unittest.TestCase):
    def setUp(self):
 
        self.filename = "test_clients.txt"
        

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding="utf-8") as f:
                pass 
        
        self.repo = RepositoryClientiFile(self.filename)

    def tearDown(self):

        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_store_client(self):
        client = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client)
        

        stored_client = self.repo.find_client(1)
        self.assertIsNotNone(stored_client)
        self.assertEqual(stored_client.get_id_client(), 1)
        self.assertEqual(stored_client.get_nume(), "Ion Popescu")
        self.assertEqual(stored_client.get_CNP(), "1234567890123")

    def test_store_client_duplicate_id(self):
        client1 = Client(1, "Ion Popescu", "1234567890123")
        self.repo.store_client(client1)
        
        client2 = Client(1, "Maria Ionescu", "9876543210987")
        with self.assertRaises(ValueError):
            self.repo.store_client(client2)

    def test_find_client(self):
        client = Client(2, "Vasile Georgescu", "1122334455667")
        self.repo.store_client(client)
        
        found_client = self.repo.find_client(2)
        self.assertIsNotNone(found_client)
        self.assertEqual(found_client.get_id_client(), 2)

    def test_find_client_not_found(self):
        client = self.repo.find_client(999)
        self.assertIsNone(client)

    def test_update_client(self):
        client = Client(3, "Ana Popa", "4455667788990")
        self.repo.store_client(client)
        
        updated_client = Client(3, "Ana Ionescu", "4455667788990")
        self.repo.update_client(updated_client)
        
        stored_client = self.repo.find_client(3)
        self.assertEqual(stored_client.get_nume(), "Ana Ionescu")

    def test_update_client_not_found(self):
        client = Client(999, "Nonexistent Client", "0000000000000")
        with self.assertRaises(ValueError):
            self.repo.update_client(client)

    def test_delete_client(self):
        client = Client(4, "Mihai Ionescu", "5566778899001")
        self.repo.store_client(client)
        
        self.repo.delete_client(4)
        
        deleted_client = self.repo.find_client(4)
        self.assertIsNone(deleted_client)

    def test_delete_client_not_found(self):
        with self.assertRaises(ValueError):
            self.repo.delete_client(999)

if __name__ == "__main__":
    unittest.main()
