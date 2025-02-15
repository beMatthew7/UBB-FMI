class Carte:
    def __init__(self, id: int, titlu: str, descriere: str, autor: str, nr_bucati):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
        self.__rental = False
        self.__nr_bucati = nr_bucati

    def get_nr_bucati(self):
        return self.__nr_bucati
    
    def set_nr_bucati(self, new_value):
        self.__nr_bucati = new_value

    def get_id_carte(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def set_titlu(self, new_value):
        self.__titlu = new_value

    def get_descriere(self):
        return self.__descriere
    
    def get_rental(self):
        return self.__rental
    
    def set_rental(self, new_value):
        self.__rental = new_value

    def set_descriere(self, value):
        self.__descriere = value

    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value
 

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)
    def __str__(self):
        return ("[" + str(self.__id) + "] Carte: Titlu = " + self.__titlu + "; Descriere = " + self.__descriere + "; Autor = " + self.__autor + "; Bucati valabile = " + str(self.__nr_bucati))
