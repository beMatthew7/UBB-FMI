import unittest


from teste.teste_domain import teste_piesa
from teste.teste_repository import teste_repository_piese
from teste.teste_service import teste_service_piesa
def run_all_tests():
    loader = unittest.TestLoader()
    

    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromModule(teste_piesa))
    suite.addTests(loader.loadTestsFromModule(teste_repository_piese))
    suite.addTests(loader.loadTestsFromModule(teste_service_piesa))
    runner = unittest.TextTestRunner()
    runner.run(suite)


