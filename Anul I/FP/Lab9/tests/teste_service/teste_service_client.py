from domain.client import Client
from domain.validation_client import ValidatorClient
from repository.repository_clienti import RepositoryClienti
from service.controller_client import ControllerClienti
from colorama import Fore, Style

def test_adauga_client_service():

    repo = RepositoryClienti()
    validator = ValidatorClient()
    service = ControllerClienti(repo, validator)


    service.adauga_client_nou(101, "Ion Popescu", "1234567890123")
    assert len(service.obtine_toti_clientii()) == 1

    try:
        service.adauga_client_nou(101, "Maria Ionescu", "2234567890123")
        assert False  
    except ValueError:
        assert True  

def test_cauta_client_service():
  
    repo = RepositoryClienti()
    validator = ValidatorClient()
    service = ControllerClienti(repo, validator)


    service.adauga_client_nou(101, "Ion Popescu", "1234567890123")

    client_gasit = service.cauta_client_dupa_id(101)
    assert client_gasit.get_nume() == "Ion Popescu"
    
   
    client_negasit = service.cauta_client_dupa_id(999)
    assert client_negasit is None

def test_filtrare_clienti_service():
 
    repo = RepositoryClienti()
    validator = ValidatorClient()
    service = ControllerClienti(repo, validator)

  
    service.adauga_client_nou(101, "Ion Popescu", "1234567890123")
    service.adauga_client_nou(102, "Maria Ionescu", "2234567890123")
    service.adauga_client_nou(103, "Ion Popescu", "3234567890123")

    
    clienti_filtrati = service.filtreaza_clienti_dupa_nume("Ion Popescu")
    assert len(clienti_filtrati) == 2
    assert all(client.get_nume() == "Ion Popescu" for client in clienti_filtrati)


    clienti_filtrati_negativi = service.filtreaza_clienti_dupa_nume("Ana Marin")
    assert len(clienti_filtrati_negativi) == 0
