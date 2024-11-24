import random
from domain.client import Client
from domain.validation_client import ValidatorClient
from repository.repository_clienti import RepositoryClienti

class ControllerClienti:
    def __init__(self, repo: RepositoryClienti, validator: ValidatorClient):
        self.__repo = repo
        self.__validator = validator

    def adauga_client_nou(self, id: int, nume: str, cnp: str):
        client = Client(id, nume, cnp)
        self.__validator.validate(client)
        self.__repo.store_client(client)

    def actualizeaza_date_client(self, id: int, nume_nou: str = None, cnp_nou: str = None):
        client_vechi = self.__repo.find_client(id)
        if client_vechi is None:
            raise ValueError("Nu există un client cu acest ID.")
        
        nume_final = nume_nou if nume_nou else client_vechi.get_nume()
        cnp_final = cnp_nou if cnp_nou else client_vechi.get_CNP()
        
        client_actualizat = Client(id, nume_final, cnp_final)
        self.__validator.validate(client_actualizat)
        self.__repo.update_client(client_actualizat)

    def cauta_client_dupa_id(self, id: int):
        return self.__repo.find_client(id)

    def sterge_client_dupa_id(self, id: int):
        client = self.__repo.find_client(id)
        if client is None:
            raise ValueError("Nu există un client cu acest ID.")
        self.__repo.delete_client(id)

    def filtreaza_clienti_dupa_nume(self, nume: str) -> list:
        return [client for client in self.__repo.get_all_clients() if client.get_nume() == nume]

    def cauta_client_pe_baza_cnp(self, cnp: str):
        for client in self.__repo.get_all_clients():
            if client.get_CNP() == cnp:
                return client
        return None
    
    def primire_id(self, client):
        return client.get_id_client


    def populeaza_clienti_impliciti(self):
        self.adauga_client_nou(201, "Ion Popescu", "1234567890123")
        self.adauga_client_nou(202, "Maria Ionescu", "2234567890123")
        self.adauga_client_nou(203, "George Enescu", "5050912226721")
        self.adauga_client_nou(204, "Ana Marin", "5050912226722")
        self.adauga_client_nou(205, "Marian Ion", "5001012438921")

    def obtine_toti_clientii(self) -> list:
        return self.__repo.get_all_clients()
    