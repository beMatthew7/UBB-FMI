from tests.teste_carte import test_carte, test_validare_carte
from tests.teste_repository_carte import test_store_repo, test_find_repo
from tests.teste_service_carte import test_adauga_carte_service, test_cauta_carte_service, test_filtrare_carti_service, test_genereaza_carti_random
from colorama import Fore, Style
from tests.teste_client import test_client, test_validare_client
from tests.teste_service_client import test_adauga_client_service, test_cauta_client_service, test_filtrare_clienti_service

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
    test_genereaza_carti_random()
    print(Fore.GREEN + "[INFO] Teste pentru Service Carti rulate cu succes." + Style.RESET_ALL)

def run_tests_client():
    test_client()
    test_validare_client()
    print(Fore.GREEN + "[INFO] Teste pentru domeniul Client rulate cu succes." + Style.RESET_ALL)

def run_tests_service_client():
    test_adauga_client_service()
    test_cauta_client_service()
    test_filtrare_clienti_service()
    print(Fore.GREEN + "[INFO] Teste pentru Service Clienti rulate cu succes." + Style.RESET_ALL)

def run_tests_all():
    run_tests_domain()
    run_tests_repository()
    run_tests_service()
    run_tests_client()
    run_tests_service_client()
    print(Fore.GREEN + "[INFO] Toate testele au rulat cu succes!" + Style.RESET_ALL)