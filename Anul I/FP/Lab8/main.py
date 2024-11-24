from domain.validation_carte import ValidatorCarte
from domain.validation_client import ValidatorClient
from repository.repository_carti import RepositoryCarti
from repository.repository_clienti import RepositoryClienti
from service.controller_carte import ControllerCarti
from service.controller_client import ControllerClienti
from tests.run_tests import run_tests_all
from ui.console import Console

run_tests_all()


validator_carte = ValidatorCarte()
repo_carti = RepositoryCarti()
book_service = ControllerCarti(repo_carti, validator_carte)

validator_client = ValidatorClient()
repo_clienti = RepositoryClienti()
client_service = ControllerClienti(repo_clienti, validator_client)



console = Console(book_service, client_service)
console.run()
