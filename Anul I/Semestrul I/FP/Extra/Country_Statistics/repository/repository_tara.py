from domain.tara import Tara

class RepositoryTara:
    def __init__(self):
        """
        Initializam o lista pentru tari
        return None
        """
        self.__tari = []

    def store(self, tara):
        """
        Adaugam o tara in lista
        :param tara: tara
        :return: None
        """
        self.__tari.append(tara)

    def get_all(self):
        """
        Returnam lista de tari
        :return: lista de tari
        """
        return self.__tari

class RepositoryTaraFile(RepositoryTara):
    def __init__(self, filename):
        """
        Initializam lista de tari din fisier
        :param filename: numele fisierului
        """
        RepositoryTara.__init__(self)
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        """
        Incarcam datele din fisier
        :return: None
        """
        with open(self.__filename, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                nume, an, inflatie, unemployment_rate, populatie = line.split(',')
                an = int(an)
                inflatie = float(inflatie)
                unemployment_rate = float(unemployment_rate)

                tara = Tara(nume, an, inflatie, unemployment_rate, populatie)
                self.store(tara)      

    def store(self, tara):
        """
        Adaugam o tara in lista
        :param tara: tara
        :return: None
        """
        super().store(tara)
        self.__save_to_file()


    def __save_to_file(self):
        """
        Salvam datele in fisier
        :return: None
        """
        with open(self.__filename, 'w') as f:
            for tara in self.get_all():
                f.write(f"{tara.get_nume()},{tara.get_an()},{tara.get_inflatie()},{tara.get_unemployment_rate()},{tara.get_populatie()}\n")              
