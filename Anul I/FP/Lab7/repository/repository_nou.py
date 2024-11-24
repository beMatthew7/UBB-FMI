from domain.carte import Carte

class RepositoryCarti:
    def __init__(self):
        self.__elements = {}  # Folosim un dicționar, unde cheia este ID-ul cărții

    def find(self, id: int) -> Carte:
        """
        Caută cartea cu id-ul dat.
        :param id: id-ul căutat
        :return: obiect de tip Carte dacă există cartea cu id-ul dat, None altfel
        """
        return self.__elements.get(id, None)

    def store(self, carte: Carte):
        """
        Adaugă o carte la bibliotecă.
        :param carte: carte de adăugat
        :return: -; biblioteca se modifică prin adăugarea cărții date
        :raises: ValueError dacă se încearcă adăugarea unei cărți cu id care există deja
        """
        if carte.get_id() in self.__elements:
            raise ValueError("Exista deja cartea cu acest id.")
        self.__elements[carte.get_id()] = carte

    def update(self, carte_actualizata: Carte):
        """
        Actualizează cartea din bibliotecă cu ID-ul specificat în obiectul carte_actualizata.
        :param carte_actualizata: carte actualizată
        :raises: ValueError dacă nu există o carte cu id-ul dat
        """
        if carte_actualizata.get_id() not in self.__elements:
            raise ValueError("Nu există cartea cu id-ul dat.")
        self.__elements[carte_actualizata.get_id()] = carte_actualizata

    def delete(self, id: int):
        """
        Șterge cartea cu id-ul dat din bibliotecă.
        :param id: ID-ul cărții de șters
        :raises: ValueError dacă nu există cartea cu id-ul specificat
        """
        if id not in self.__elements:
            raise ValueError("Nu există o carte cu acest ID.")
        del self.__elements[id]

    def get_all(self) -> list:
        """
        Returnează toate cărțile din bibliotecă.
        :return: o listă cu toate obiectele Carte
        """
        return list(self.__elements.values())

    def get_size(self) -> int:
        """
        Returnează numărul de cărți din bibliotecă.
        :return: numărul de cărți
        """
        return len(self.__elements)
