import random
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte
from repository.repository_carti import RepositoryCarti


class ControllerCarti:
    def __init__(self, repo: RepositoryCarti, validator: ValidatorCarte):
        self.__repo = repo
        self.__validator = validator

    def adauga_carte(self, id, titlu, descriere, autor, nr_bucati):
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
        c = Carte(id, titlu, descriere, autor, nr_bucati)
        self.__validator.validate(c)
        self.__repo.store_book(c)

    def actualizeaza_carte(self, id: int, titlu_nou: str = None, descriere_noua: str = None, autor_nou: str = None, nr_bucati_nou: int = 0):
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


        c_new = Carte(id, titlu_nou, descriere_noua, autor_nou, nr_bucati_nou)
        self.__validator.validate(c_new)
        self.__repo.update_book(c_new)

    def verificare_inchiriere(self, carte):
        return carte.get_rental()
    
    def find_carte(self, id: int):
        """
        Cauta cartea cu id dat
        :param id: id-ul dupa care se cauta
        :return: cartea cu id-ul dat, daca aceasta exista, None altfel
        """
        return self.__repo.find_book(id)


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
        self.adauga_carte(101, "Dune", "Un roman clasic despre dragoste și prejudecăți în Anglia secolului XIX", "Frank Herbert", 20)
        self.adauga_carte(102, "1984", "O distopie despre un viitor controlat de supraveghere totalitară", "George Orwell", 20)
        self.adauga_carte(103, "Room", "Un roman captivant despre supraviețuire", "Emma Donoghue", 20)
        self.adauga_carte(104, "Jazz", "O meditație asupra iubirii", "Toni Morrison", 20)
        self.adauga_carte(105, "Heat", "O poveste despre pasiunea pentru baseball și relațiile de familie", "Mike Lupica", 20)

    def cauta_carte_dupa_titlu_si_autor(self, titlu, autor):
        for carte in self.__repo.get_all_books():
            if carte.get_titlu() == titlu and carte.get_autor() == autor:
                return carte
        return None
    def get_all_books(self) -> list:
        """
        Returneaza biblioteca de carti
        :return:
        """
        return self.__repo.get_all_books()


    def genereaza_carti_random(self, x):
        """
        Generează și adaugă X cărți aleatorii utilizând recursivitate.
        Dacă ID-ul unei cărți există deja, încearcă alt ID, fără a scădea numărul total de generat.
        """
        if x == 0:
            return  

        import random
        id = random.randint(1, 10)
        titlu = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=random.randint(5, 20)))
        descriere = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz ", k=random.randint(20, 100)))
        autor = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=random.randint(5, 20)))
        nr_bucati = random.randint(2, 100)

        try:
            self.adauga_carte(id, titlu, descriere, autor, nr_bucati)

            self.genereaza_carti_random(x - 1)
        except ValueError:
 
            self.genereaza_carti_random(x)

    def sortare_mixta(self):
        """
        Sortează cărțile dupa autor, apoi dupa titlu.
        """
        lista_carti = self.__repo.get_all_books()
        return self.bubble_sort(lista_carti)
        
    def compara_carti(self, carte1, carte2):
        """
        Compară două cărți după autor, apoi după titlu.
        :param carte1: Prima carte de comparat
        :param carte2: A doua carte de comparat
        :return: -1 dacă prima carte este mai mică, 1 dacă este mai mare, 0 dacă sunt egale
        """
        if carte1.get_autor() < carte2.get_autor():
            return -1
        elif carte1.get_autor() > carte2.get_autor():
            return 1
        else:  
            if carte1.get_titlu() < carte2.get_titlu():
                return -1
            elif carte1.get_titlu() > carte2.get_titlu():
                return 1
            else:
                return 0



    def bubble_sort(self, lista_carti):
        """
        Sortează lista de cărți folosind algoritmul Bubble Sort.
        :param lista_carti: Lista de cărți de sortat
        :param compara: Funcția de comparare a cărților
        :return: Lista de cărți sortată
        """
        n = len(lista_carti)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.compara_carti(lista_carti[j], lista_carti[j + 1]) > 0:
                    lista_carti[j], lista_carti[j + 1] = lista_carti[j + 1], lista_carti[j]
        return lista_carti      