import random
from domain.client import Client
from domain.validation_client import ValidatorClient
from repository.repository_clienti import RepositoryClienti

class ControllerClienti:
    def __init__(self, repo: RepositoryClienti, validator: ValidatorClient):
        """
        Inițializează controller-ul pentru gestionarea clienților.
        :param repo: repository-ul pentru stocarea clienților
        :param validator: validatorul pentru validarea obiectelor Client
        """
        self.__repo = repo
        self.__validator = validator

    def adauga_client_nou(self, id: int, nume: str, cnp: str):
        """
        Adaugă un client nou.
        :param id: ID-ul clientului
        :param nume: numele clientului
        :param cnp: codul numeric personal al clientului
        :raises ValueError: dacă datele clientului sunt invalide sau ID-ul există deja
        """
        client = Client(id, nume, cnp)
        self.__validator.validate(client)
        self.__repo.store_client(client)

    def actualizeaza_date_client(self, id: int, nume_nou: str = None, cnp_nou: str = None):
        """
        Actualizează datele unui client existent.
        :param id: ID-ul clientului
        :param nume_nou: noul nume al clientului (opțional)
        :param cnp_nou: noul CNP al clientului (opțional)
        :raises ValueError: dacă clientul nu există sau noile date sunt invalide
        """
        client_vechi = self.__repo.find_client(id)
        if client_vechi is None:
            raise ValueError("Nu există un client cu acest ID.")
        
        nume_final = nume_nou if nume_nou else client_vechi.get_nume()
        cnp_final = cnp_nou if cnp_nou else client_vechi.get_CNP()
        
        client_actualizat = Client(id, nume_final, cnp_final)
        self.__validator.validate(client_actualizat)
        self.__repo.update_client(client_actualizat)

    def cauta_client_dupa_id(self, id: int):
        """
        Caută un client după ID.
        :param id: ID-ul clientului
        :return: clientul găsit sau None dacă nu există
        """
        return self.__repo.find_client(id)

    def sterge_client_dupa_id(self, id: int):
        """
        Șterge un client după ID.
        :param id: ID-ul clientului de șters
        :raises ValueError: dacă clientul nu există
        """
        self.__repo.delete_client(id)

    def filtreaza_clienti_dupa_nume(self, nume: str, clienti=None, index=0) -> list:
        """
        Filtrează clienții după nume folosind recursivitate.
        :param nume: numele după care se filtrează
        :param clienti: lista clienților din repo (opțional, folosită intern pentru recursivitate)
        :param index: indexul curent din lista de clienți
        :return: lista clienților care au numele specificat
        """
        if clienti is None:
            clienti = self.__repo.get_all_clients()  

        if index == len(clienti):
            return []

        client = clienti[index]
        if client.get_nume() == nume:
            return [client] + self.filtreaza_clienti_dupa_nume(nume, clienti, index + 1)
        else:
            return self.filtreaza_clienti_dupa_nume(nume, clienti, index + 1)

    def cauta_client_pe_baza_cnp(self, cnp: str):
        """
        Caută un client pe baza CNP-ului.
        :param cnp: codul numeric personal al clientului
        :return: clientul găsit sau None dacă nu există
        """
        for client in self.__repo.get_all_clients():
            if client.get_CNP() == cnp:
                return client
        return None

    def primire_id(self, client):
        """
        Obține ID-ul unui client.
        :param client: obiectul Client
        :return: ID-ul clientului
        """
        return client.get_id_client()

    def populeaza_clienti_impliciti(self):
        """
        Adaugă o listă de clienți predefiniți în repository.
        :return: -
        """
        self.adauga_client_nou(201, "Ion Popescu", "1234567890123")
        self.adauga_client_nou(202, "Maria Ionescu", "2234567890123")
        self.adauga_client_nou(203, "George Enescu", "5050912226721")
        self.adauga_client_nou(204, "Ana Marin", "5050912226722")
        self.adauga_client_nou(205, "Marian Ion", "5001012438921")

    def obtine_toti_clientii(self) -> list:
        """
        Returnează toți clienții din repository.
        :return: lista tuturor clienților
        """
        return self.__repo.get_all_clients()
