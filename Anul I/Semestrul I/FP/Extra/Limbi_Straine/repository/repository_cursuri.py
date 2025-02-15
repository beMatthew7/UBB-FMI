from domain.curs import Curs

class RepositoryCursuri:
    def __init__(self):
        self.__cursuri = []

    def store(self, curs):
        """
        Adauga un curs in lista de cursuri
        :param curs: cursul care se adauga
        :return: -
        """
        self.__cursuri.append(curs)
        
    def get_all(self):
        """
        Returneaza lista de cursuri
        :return: lista de cursuri
        """
        return self.__cursuri

class RepositoryCursuriFile(RepositoryCursuri):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r', coding = "utf-8") as f:
                for line in f:
                    try:
                        id_curs, limba_straina, nivel, pret = line.strip().split(',')
                        pret = int(pret)
                    except ValueError:
                        print(f"Linia {line} nu este valida")
                        continue
                    curs = Curs(id_curs, limba_straina, nivel, pret)
                    super().store(curs)
        except FileNotFoundError:
            print("Fisierul nu exista")

    def __save_to_file(self):
        with open(self.__filename, 'w') as f:
            for curs in self.get_all():
                f.write(f"{curs.get_id_curs()},{curs.get_limba_straina()},{curs.get_nivel()},{curs.get_pret()}\n")

    def store(self, curs):
        super().store(curs)
        self.__save_to_file()
