from domain.produs import Produs

class ControllerProdus:
    def __init__(self, repo):
        self.__repo = repo


    def adauga_produs(self, id, denumire, pret):
        """
        Adaugam un produs in memorie
        :param id: id-ul produsului
        :param denumire: denumirea produsului
        :param pret: pretul produsului
        :return: None
        """
        produs1 = Produs(id, denumire, pret)
        for produs in self.__repo.get_all():
            if produs.get_id() == id:
                raise Exception("Un produs cu acest id exista deja")
        self.__repo.store(produs1)

    def sterge_produs(self, cifra):
        """
        Stergem toate elementele care contin o anumita cifra in id
        :param: cifra cifra introdusa de catre utilizator
        :return : None
        """        
        produse_gasite = 0
        if(cifra < 0 or cifra > 9):
            raise Exception("Cifra trebuie sa fie un numar intre 0 si 9")
        for produs in self.__repo.get_all():
            id = produs.get_id()
            while id > 0:
                if id % 10 == cifra:
                    self.__repo.delete(produs.get_id())
                    produse_gasite += 1
                id = id // 10

        if(produse_gasite == 0):
            raise Exception("Nu exista produse care sa contina aceasta cifra")         
        
    def filtrare_produse(self, text, numar):
        """
        Filtram lista de produse astfel incat sa fie afisate dooar cele care conti un anumit text si pretul este mai mic fata de un anumit numar
        :param text: textul introdus de catre utilizator
        :param numar: numarul introdus de catre utilizator
        :return: lista filtrata
        """
        lista_filtrata = []
        for produs in self.__repo.get_all():
            if (text in produs.get_denumire() or text == "") and (produs.get_pret() < numar or numar == -1):
                lista_filtrata.append(produs)
        return lista_filtrata

 
    def undo(self):
        """
        Undo la ultima operatie de adaugare sau stergere
        """
        self.__repo.undo()