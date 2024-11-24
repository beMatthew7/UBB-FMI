from domain.carte import Carte


class RepositoryCarti:
    def __init__(self):
        self.__elements = []

    def find_book(self, id: int)->Carte:
        """
        Cauta melodia cu id dat
        :param id: id-ul cautat
        :return: obiect de tip Carte daca exista carte cu id dat, None altfel
        """
        for carte in self.__elements:
            if carte.get_id_carte() == id:
                return carte
        return None

    def store_book(self, carte: Carte):
        """
        Adauga o carte la bilbioteca
        :param carte: carte de adaugat
        :return: -; bilbioteca se modifica prin adaugarea cartii date
                postconditie: melodie apartine bilbioteca
        :raises: ValueError daca se incearca adaugarea unei cartu cu id care exista deja
        """
        if self.find_book(carte.get_id_carte()) is not None:
            raise ValueError("Exista deja cartea cu acest id.")
        self.__elements.append(carte)

    def __find_pos_book(self, id: int):
        """
        Gaseste pozitia in lista a cartii cu id dat (daca o astfel de melodie exista)
        :param id: id-ul cautat
        :return: pozitia in lista a cartii cu id dat, pos returnat intre 0 si len(self.__elements) daca, cartea exista
                -1 daca nu exista cartea cu id dat
        """
        pos = -1
        for index, carte in enumerate(self.__elements):
            if carte.get_id_carte() == id:
                pos = index
                break
        return pos

    def update_book(self, carte_actualizata):
        """
        Actualizeaza melodia din lista cu ID = id-ul cartii date ca parametru
        :param carte_actualizata: carte actualizata
        :return:
        """
        pos = self.__find_pos_book(carte_actualizata.get_id_carte())
        if pos == -1:
            raise ValueError("Nu exista melodie cu id dat.")
        self.__elements[pos] = carte_actualizata

    def delete_book(self, id: int):
        """
        Șterge cartea cu id-ul dat din bibliotecă.
        :param id: ID-ul cărții de șters
        :raises: ValueError dacă nu există cartea cu id-ul specificat
        """
        pos = self.__find_pos(id)
        if pos == -1:
            raise ValueError("Nu există o carte cu acest ID.")
        
        del self.__elements[pos]


    def get_all_books(self) -> list:
        """
        Returneaza colectia de melodii
        :return: colectia de melodii
        """
        return self.__elements
