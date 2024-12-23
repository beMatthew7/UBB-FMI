class Inchiriere:
    def __init__(self, carte, client, nr_inchirieri=1):
        """
        Initializează o închiriere.
        :param carte: Obiect de tip Carte
        :param client: Obiect de tip Client
        :param nr_inchirieri: Numărul total de închirieri (default 1)
        """
        self.__carte = carte
        self.__client = client
        self.__nr_inchirieri = nr_inchirieri
    def get_carte(self):
        return self.__carte

    def get_client(self):
        return self.__client

    def get_nr_inchirieri(self):
        return self.__nr_inchirieri

    def is_returnata(self):
        return self.__returnata

    def set_nr_inchirieri(self, nr):
        self.__nr_inchirieri = nr

    def set_returnata(self, status):
        self.__returnata = status

    def __str__(self):
        status = "returnată" if self.__returnata else "ne-returnată"
        return f"Cartea: {self.__carte} este închiriată de {self.__client}. Status: {status}, Număr de închirieri: {self.__nr_inchirieri}"
