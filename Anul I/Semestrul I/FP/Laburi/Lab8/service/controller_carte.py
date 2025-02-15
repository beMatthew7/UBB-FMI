import random
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte
from repository.repository_carti import RepositoryCarti


class ControllerCarti:
    def __init__(self, repo: RepositoryCarti, validator: ValidatorCarte):
        self.__repo = repo
        self.__validator = validator

    def adauga_carte(self, id, titlu, descriere, autor):
        """
        Adauga o melodie
        :param id: id-ul cartii de adaugat
        :param titlu: titlul cartii pe care vrem sa o adaugam
        :param autor: autorul cartii pe care vrem sa o adaugam
        :param descriere: descriere cartii pe care vrem sa o adaugam
        :param durata: durata melodiei pe care vrem sa o adaugam
        :return: -; lista data se modifica prin adaugarea cartii cu informatiile date
        :raises: ValueError daca cartea nu este valida
                 ValueError daca exista deja cartea cu id dat
        """
        c = Carte(id, titlu, descriere, autor)
        self.__validator.validate(c)
        self.__repo.store_book(c)

    def actualizeaza_carte(self, id: int, titlu_nou: str = None, descriere_noua: str = None, autor_nou: str = None):
        """
        Actualizează cartea cu id-ul specificat, folosind informațiile noi date.
        Doar atributele specificate vor fi actualizate.
        
        :param id: id-ul cărții de actualizat
        :param titlu_nou: noul titlu al cărții (opțional)
        :param descriere_noua: noua descriere a cărții (opțional)
        :param autor_nou: noul autor al cărții (opțional)
        :return: -; lista de cărți se modifică prin actualizarea cărții cu id-ul specificat,
                    dacă o carte cu acest id există
        :raises: ValueError dacă informațiile date nu pot construi o carte validă
                ValueError dacă nu există o carte cu id-ul dat
        """


        c_new = Carte(id, titlu_nou, descriere_noua, autor_nou)
        self.__validator.validate(c_new)
        self.__repo.update_book(c_new)

    def find_carte(self, id: int):
        """
        Cauta cartea cu id dat
        :param id: id-ul dupa care se cauta
        :return: cartea cu id-ul dat, daca aceasta exista, None altfel
        """
        return self.__repo.find(id)


    def delete_carte(self, id: int):
        """
        Șterge cartea cu id-ul dat din colecție.
        :param id: ID-ul cărții de șters
        :raises: ValueError dacă nu există o carte cu acest ID în colecție
        """

        carte = self.__repo.find_book(id)
        if carte is None:
            raise ValueError("Nu există o carte cu acest ID.")
        
        self.__repo.delete_book(id)


    def filtreaza_dupa_autor(self, autor: str) -> list:
        """
        Filtrează cărțile după autorul specificat.
        :param autor: Autorul cărților de filtrat
        :return: Lista de cărți scrise de autorul specificat
        """
        return [carte for carte in self.__repo.get_all_books() if carte.get_autor() == autor]


    def cauta_carte_dupa_titlu(self, titlu: str):
        """
        Caută o carte după titlu.
        :param titlu: Titlul cărții de căutat
        :return: Cartea găsită cu titlul specificat, sau None dacă nu există
        """
        for carte in self.__repo.get_all_books():
            if carte.get_titlu() == titlu:
                return carte
        return None


    def add_default(self):
        self.adauga_carte(201, "Mândrie și prejudecată", "Un roman clasic despre dragoste și prejudecăți în Anglia secolului XIX", "Jane Austen")
        self.adauga_carte(202, "1984", "O distopie despre un viitor controlat de supraveghere totalitară", "George Orwell")
        self.adauga_carte(203, "Micul Prinț", "Povestea fermecătoare a unui prinț și a călătoriilor sale", "Antoine de Saint-Exupéry")
        self.adauga_carte(204, "Crimă și pedeapsă", "O analiză psihologică a unui om care comite o crimă și se confruntă cu urmările morale", "Fiodor Dostoievski")


    def get_all_books(self) -> list:
        """
        Returneaza biblioteca de carti
        :return:
        """
        return self.__repo.get_all_books()


    def genereaza_carti_random(self, x):
        """
        Generează și adaugă X cărți aleatorii.
        Dacă ID-ul unei cărți există deja, încearcă alt ID, fără a scădea numărul total de generat.
        """
        import random
        carti_generate = 0

        while carti_generate < x:
            id = random.randint(1, 10)
            titlu = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=random.randint(5, 20)))
            descriere = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz ", k=random.randint(20, 100)))
            autor = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=random.randint(5, 20)))

            try:
                self.adauga_carte(id, titlu, descriere, autor)
                carti_generate += 1
            except ValueError:
                pass
