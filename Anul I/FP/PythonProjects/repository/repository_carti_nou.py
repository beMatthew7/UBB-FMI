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

    def update_book(self, carte_noua: Carte):
        """
        Actualizeaza cartea cu id-ul dat
        :param carte_noua: cartea cu noile date
        :return: -; cartea se actualizeaza
        :raises: ValueError daca nu exista o cartea cu id-ul dat
        """
        pos = self.__find_pos_book(carte_noua.get_id_carte())
        if pos == -1:
            raise ValueError("Nu există o carte cu acest ID.")
        self.__elements[pos] = carte_noua

    def delete_book(self, id: int):
        """
        Șterge cartea cu id-ul dat din bibliotecă.
        :param id: ID-ul cărții de șters
        :raises: ValueError dacă nu există cartea cu id-ul specificat
        """
        pos = self.__find_pos_book(id)
        if pos == -1:
            raise ValueError("Nu există o carte cu acest ID.")
        
        del self.__elements[pos]


    def get_all_books(self) -> list:
        """
        Returneaza colectia de melodii
        :return: colectia de melodii
        """
        return self.__elements
    

class RepositoryCartiFile(RepositoryCarti):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citeste datele din fisier
        """
        with open(self.__filename, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line: 
                    continue
                try:
                    id, titlu, descriere, autor, nr_bucati = line.split('\n')
                    id = int(id)
                    nr_bucati = int(nr_bucati)
                    carte = Carte(id, titlu.strip(), descriere.strip(), autor.strip(), nr_bucati)
                    super().store_book(carte)
                except ValueError as e:
                    print(f"Eroare la procesarea liniei: '{line}' - {e}")


    def __save_to_file(self):
        """
        Salveaza datele in fisier
        """
        with open(self.__filename, 'w', encoding="utf-8") as file:
            for carte in self.get_all_books():
                file.write(f"{carte.get_id_carte()}\n{carte.get_titlu()}\n{carte.get_descriere()}\n{carte.get_autor()}\n{carte.get_nr_bucati()}\n")
                file.flush() 
 


    def store_book(self, carte: Carte):
        """
        Adauga carte la biblioteca si salveaza in fisier
        :param carte: carte de adaugat
        :return: -;
        """
        super().store_book(carte)
        self.__save_to_file()

    def update_book(self, carte_actualizata):
        """
        Actualizeaza cartea din biblioteca si salveaza in fisier
        :param carte_actualizata: carte actualizata
        :return: -;
        """
        super().update_book(carte_actualizata)
        self.__save_to_file()

    def delete_book(self, id: int):
        """
        Sterge cartea cu id-ul dat din biblioteca si salveaza in fisier
        :param id: id-ul cartii de sters
        :return: -
        """
        super().delete_book(id)
        self.__save_to_file()    
