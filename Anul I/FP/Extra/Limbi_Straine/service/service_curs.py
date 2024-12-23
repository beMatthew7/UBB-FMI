class ControllerCurs:
    def __init__(self, repo):
        self.__repo = repo

    def cauta_curs(self, limba_straina):
        """"
        Cauta cursul cu limba straina data
        :param limba_straina: limba straina data
        :return: cursul cu limba straina data
        """
        #limba straina trebuie sa fie continua de curs get limba
        cursuri_disponibile = []
        cursuri = self.__repo.get_all()
        for curs in cursuri:
            limba = str(curs.get_limba_straina())
            if limba_straina in limba:
                cursuri_disponibile.append(curs)
        

        if(cursuri_disponibile == []):
            raise Exception("Nu exista cursuri disponibile")
        
        return cursuri_disponibile

    def inscriere_curs(self, id_curs, numar_ore):
        """
        Inscrie un curs
        :param id_curs: id-ul cursului
        :param numar_ore: numarul de ore
        :return: -
        """
        cursuri = self.__repo.get_all()
        for curs in cursuri:
            if curs.get_id_curs() == id_curs:
                pret = curs.get_pret()
                break
        else:
            raise Exception("Cursul nu exista")

        if numar_ore < 1:
            raise Exception("Numarul de ore trebuie sa fie mai mare decat 0")
        
        total = pret * numar_ore
        inscriere = f"{curs.get_limba_straina()},{curs.get_nivel()},{total}"
        return inscriere