from domain.inchiriere import Inchiriere

class RepoInchirieri:
    def __init__(self):
        self.__inchirieri = []

    def sterge_inchiriere(self, inchiriere):
        """
        Șterge o închiriere din lista de închirieri.
        :param inchiriere: Închirierea de șters.
        """
        self.__inchirieri.remove(inchiriere)

    def adauga_inchiriere(self, inchiriere):
        """
        adauga o inchiriere la lista de inchirieri
        :param inchiriere Inchiriere de sters
        """
        self.__inchirieri.append(inchiriere)

    def get_all(self):
        """
        retruneaza toate inchirierile din lista
        """
        return self.__inchirieri


class RepositoryInchirieriFile(RepoInchirieri):
    def __init__(self, filename, repo_carti, repo_clienti):
        super().__init__()
        self.__filename = filename
        self.__repo_carti = repo_carti  
        self.__repo_clienti = repo_clienti 
        self.__load_from_file()

    def __load_from_file(self):
        """
        Încarcă închirierile din fișier.
        """
        try:
            with open(self.__filename, 'r') as file:
                for line in file:
                    id_carte,tiltu,autor, nr_inchirieri,id_client,nume_client,cnp_client = line.strip().split(',')
                    
                    carte = self.__repo_carti.find_book(int(id_carte))  
                    client = self.__repo_clienti.find_client(int(id_client))  
                    inchiriere = Inchiriere(carte, client, int(nr_inchirieri))
                    super().adauga_inchiriere(inchiriere)
        except FileNotFoundError:
            print(f"Fișierul {self.__filename} nu a fost găsit.")
    def __save_to_file(self):
        """
        Salvează închirierile în fișier.
        """
        with open(self.__filename, 'a') as file:
            for inchiriere in self.get_all():

                id_carte = inchiriere.get_carte().get_id_carte()  
                nume_carte = inchiriere.get_carte().get_titlu()    
                autor_carte = inchiriere.get_carte().get_autor() 

                nr_inchirieri_carte = inchiriere.get_nr_inchirieri() 


                id_client = inchiriere.get_client().get_id_client()  
                nume_client = inchiriere.get_client().get_nume()     
                cnp_client = inchiriere.get_client().get_CNP()       
               


                file.write(f"{id_carte},{nume_carte},{autor_carte},{nr_inchirieri_carte},"
                        f"{id_client},{nume_client},{cnp_client}\n")


    def adauga_inchiriere(self, inchiriere: Inchiriere):
        """
        Adaugă închiriere la lista și salvează în fișier.
        """
        super().adauga_inchiriere(inchiriere)
        self.__save_to_file()

    def returneaza_carte(self, inchiriere: Inchiriere):
        """
        Șterge închiriere din listă și salvează în fișier.
        """
        super().sterge_inchiriere(inchiriere)
        self.__save_to_file()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
