from domain.validation import ValidatorCarte
from repository.repository_nou import RepositoryCarti
from service.controller import ControllerCarti
from tests.run_tests import run_tests_all
from ui.console import Console

run_tests_all()

validator = ValidatorCarte()
repo = RepositoryCarti()
book_service = ControllerCarti(repo, validator)
console = Console(book_service)
console.run()


