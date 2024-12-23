from tests.teste_domain import teste_carte, teste_client, test_inchiriere
from tests.teste_repository import teste_repository_carte, teste_repository_clienti, teste_repository_inchiriere
from tests.teste_service import teste_service_carte, teste_service_client, teste_service_inchiriere
import unittest

def run_all_tests():
    loader = unittest.TestLoader()
    

    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_inchiriere))
    suite.addTests(loader.loadTestsFromModule(teste_carte))
    suite.addTests(loader.loadTestsFromModule(teste_client))
    suite.addTests(loader.loadTestsFromModule(teste_repository_carte))
    suite.addTests(loader.loadTestsFromModule(teste_repository_clienti))
    suite.addTests(loader.loadTestsFromModule(teste_service_carte))
    suite.addTests(loader.loadTestsFromModule(teste_service_client))
    suite.addTests(loader.loadTestsFromModule(teste_service_inchiriere))
    

    runner = unittest.TextTestRunner()
    runner.run(suite)
