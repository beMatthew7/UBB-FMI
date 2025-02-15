from domain.produs import Produs

class RepositoryProduse:
    def __init__(self):
        """
        Initializam o lista unde vor fi puse produsele
        """
        self.__produse = []
        self.__undo = []

    def undo(self):
        """
        Undo la ultima operatie de stergere
        """
        if len(self.__undo) > 0:
            self.__produse = self.__undo.pop()
        else:
            raise Exception("Nu se poate face undo")   

    def store(self, produs : Produs):
        """
        Adaugam un produs in lista
        :param produs: produsul care trebuie adaugat
        :return: None
        """
        self.__produse.append(produs)

    def delete(self, id):
        """
        Stergem un produs din lista
        :param id: id-ul produsului care trebuie sters
        :return: None
        """
        for produs in self.__produse:
            if produs.get_id() == id:
                self.__undo.append(self.__produse.copy())
                self.__produse.remove(produs)
                return
            
    def get_all(self):
        """
        Returnam lista de produse
        :return: lista de produse
        """
        return self.__produse         


class RepositoryProduseFile(RepositoryProduse):
    def __init__(self, filename):
        """
        Initializam un fisier unde vor fi puse produsele
        """
        RepositoryProduse.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarcam produsele din fisier
        """
        try:
            with open(self.__filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    id, denumire, pret = line.strip().split(',')
                    produs = Produs(int(id), denumire, float(pret))
                    self.store(produs)
        except FileNotFoundError:
            print("File not found")

    def store(self, produs):
        """
        Adaugam un produs in fisier si in memorie
        :param produs: produsul care trebuie adaugat
        :return: None
        """
        RepositoryProduse.store(self, produs)
        self.__save_to_file()

    def __save_to_file(self):
        """
        Salvam produsele in fisier
        """
        with open(self.__filename, 'w') as file:
            for produs in self.get_all():
                file.write(f"{produs.get_id()},{produs.get_denumire()},{produs.get_pret()}\n")    


    def delete(self, id):
        """
        Stergem un produs din fisier si din memorie
        :param id: id-ul produsului care trebuie sters
        :return: None
        """
        super().delete(id)
        self.__save_to_file()
        
    def undo(self):
        """
        Undo la ultima operatie de stergere
        """
        super().undo()
        self.__save_to_file()        