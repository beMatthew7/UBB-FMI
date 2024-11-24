import unittest
from domain.client import Client
from repository.repository_clienti import RepositoryClienti

class TestRepositoryClienti(unittest.TestCase):

    def setUp(self):
        self.repo = RepositoryClienti()
        self.client1 = Client(101, "Ion Popescu", "1234567890123")
        self.client2 = Client(102, "Maria Ionescu", "2234567890123")
        self.client3 = Client(103, "George Enescu", "3234567890123")
        
    def test_store(self):
        self.repo.store(self.client1)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.find(101), self.client1)

    def test_find(self):
        self.repo.store(self.client1)
        client_found = self.repo.find(101)
        self.assertEqual(client_found, self.client1)
        self.assertIsNone(self.repo.find(999)) 
    
    def test_update(self):
        self.repo.store(self.client1)
        self.client1.set_nume("Ion Popescu Updated")
        self.repo.update(self.client1)
        updated_client = self.repo.find(101)
        self.assertEqual(updated_client.get_nume(), "Ion Popescu Updated")
        


    def test_delete(self):
        self.repo.store(self.client1)
        self.repo.store(self.client2)
        self.repo.delete(101)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertIsNone(self.repo.find(101)) 

    def test_get_all(self):
        self.repo.store(self.client1)
        self.repo.store(self.client2)
        all_clients = self.repo.get_all()
        self.assertEqual(len(all_clients), 2)
        self.assertIn(self.client1, all_clients)
        self.assertIn(self.client2, all_clients)

    def test_find_pos(self):
        self.repo.store(self.client1)
        self.repo.store(self.client2)
        pos = self.repo._RepositoryClienti__find_pos(101)  
        self.assertEqual(pos, 0)
        
