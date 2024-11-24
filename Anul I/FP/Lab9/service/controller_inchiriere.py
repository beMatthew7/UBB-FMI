from domain.inchiriere import Inchiriere
from repository.repository_inchirieri import RepoInchirieri

class ControllerInchirieri:
    def __init__(self, repo_inchirieri : RepoInchirieri):
        self.__repo_inchirieri = repo_inchirieri

    def adauga_inchiriere(self, carte, client):
        inchiriere = Inchiriere(carte, client)
        self.__repo_inchirieri.adauga_inchiriere(inchiriere)

    def returneaza_carte(self, inchiriere):
        inchiriere.set_returnata(True)

    def cele_mai_inchiriate_carti(self):
        statistici = {}
        for inchiriere in self.__repo_inchirieri.get_all():
            carte = inchiriere.get_carte()
            if carte not in statistici:
                statistici[carte] = 0
            statistici[carte] += inchiriere.get_nr_inchirieri()
        return sorted(statistici.items(), key=lambda x: x[1], reverse=True)

    def clienti_ord_desch_numar_carti(self):
        statistici = {}
        for inchiriere in self.__repo_inchirieri.get_all():
            client = inchiriere.get_client()
            if client not in statistici:
                statistici[client] = 0
            statistici[client] += 1
        return sorted(statistici.items(), key=lambda x: x[1], reverse=True)

    def primii_20_proc_activi(self):
        clienti_ordonati = self.clienti_ord_desch_numar_carti()
        top_20_percent = int(len(clienti_ordonati) * 0.2)
        if(top_20_percent == 0):
            top_20_percent = 1
        return clienti_ordonati[:top_20_percent]

    def cauta_inchiriere_dupa_carte_si_client(self, carte, client):
        for inchiriere in self.__repo_inchirieri.get_all():
            if inchiriere.get_carte() == carte and inchiriere.get_client() == client:
                return inchiriere
        return None
