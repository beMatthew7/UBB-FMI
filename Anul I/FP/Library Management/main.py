from domain.validation_carte import ValidatorCarte
from domain.validation_client import ValidatorClient
from repository.repository_carti import RepositoryCartiFile
from repository.repository_clienti import RepositoryClientiFile
from repository.repository_inchirieri import RepositoryInchirieriFile
from service.controller_inchiriere import ControllerInchirieri
from service.controller_carte import ControllerCarti
from service.controller_client import ControllerClienti
from tests.run_tests import run_all_tests
from ui.console import Console
run_all_tests()


validator_carte = ValidatorCarte()
repo_carti = RepositoryCartiFile("PythonProjects/data/carti.txt")
book_service = ControllerCarti(repo_carti, validator_carte)

validator_client = ValidatorClient()
repo_clienti = RepositoryClientiFile("PythonProjects/data/clienti.txt")
client_service = ControllerClienti(repo_clienti, validator_client)

repo_inchirieri = RepositoryInchirieriFile("PythonProjects/data/inchirieri.txt", repo_carti, repo_clienti)
rental_service = ControllerInchirieri(repo_inchirieri)



console = Console(book_service, client_service, rental_service)
console.run()
