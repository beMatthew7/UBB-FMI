from domain.piesa import Piesa

class RepositoryPiese:
    def __init__(self):
        self._piese = {}

    def store(self, piesa: Piesa):
        """
        Adauga piesa de teatru la lista
        :param piesa: piesa de teatru
        :return: -
        """
        piesa_key = piesa.get_titlu() + '_' + piesa.get_regizor()
        if piesa_key in self._piese:
            raise KeyError("Piesa deja exista.")
        self._piese[piesa_key] = piesa
    def update(self, piesa: Piesa):
        """
        Modifica piesa de teatru
        :param piesa: piesa de teatru
        :return: -
        """
        piesa_key = piesa.get_titlu() + '_' + piesa.get_regizor()
        if piesa_key not in self._piese:
            raise KeyError("Piesa nu exista.")
        self._piese[piesa_key] = piesa

    def get_all(self):
        """
        Returneaza lista de piese
        :return: lista de piese
        """
        return list(self._piese.values())


class RepositoryPieseFile(RepositoryPiese):
    def __init__(self, filename):
        RepositoryPiese.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as file:
                for line in file:
                    titlu, regizor, gen, durata = line.strip().split(',')
                    piesa = Piesa(titlu, regizor, gen, int(durata))
                    self.store(piesa)
        except FileNotFoundError:
            print("Fisierul nu exista.")

    def store(self, piesa: Piesa):
        super().store(piesa)
        self.__save_to_file()

    def __save_to_file(self):
        with open(self.__filename, 'w') as file:
            for piesa in self.get_all():
                file.write(f"{piesa.get_titlu()},{piesa.get_regizor()},{piesa.get_gen()},{piesa.get_durata()}\n")       

    def update(self, piesa: Piesa):
        super().update(piesa)
        self.__save_to_file()      