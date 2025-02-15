
from tests.teste_carte import test_carte, test_validare_carte
from tests.teste_repository import test_store_repo, test_find_repo
from tests.teste_service import test_adauga_carte_service, test_cauta_carte_service, test_filtrare_carti_service
from colorama import Fore, Style

def run_tests_domain():
    test_carte()
    test_validare_carte()
    print(Fore.GREEN + "[INFO] Teste pentru domeniul Carte rulate cu succes." + Style.RESET_ALL)

def run_tests_repository():
    test_store_repo()
    test_find_repo()
    print(Fore.GREEN + "[INFO] Teste pentru Repository Carti rulate cu succes." + Style.RESET_ALL)

def run_tests_service():
    test_adauga_carte_service()
    test_cauta_carte_service()
    test_filtrare_carti_service()
    print(Fore.GREEN + "[INFO] Teste pentru Service Carti rulate cu succes." + Style.RESET_ALL)

def run_tests_all():
    run_tests_domain()
    run_tests_repository()
    run_tests_service()

