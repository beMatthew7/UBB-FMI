from domain.inchiriere import Inchiriere
from repository.repository_inchirieri import RepoInchirieri

class ControllerInchirieri:
    def __init__(self, repo_inchirieri: RepoInchirieri):
        """
        Constructor pentru controllerul de închirieri, care gestionează interacțiunile
        cu repo-ul de închirieri.
        :param repo_inchirieri: Repo-ul care gestionează lista de închirieri.
        """
        self.__repo_inchirieri = repo_inchirieri

    def adauga_inchiriere(self, carte, client):
        """
        Adaugă o nouă închiriere în sistem.
        :param carte: Cartea care va fi închiriată.
        :param client: Clientul care închiriază cartea.
        :return: -; lista de închirieri se modifică prin adăugarea unei noi închirieri.
        :raises: ValueError dacă există deja o închiriere activă pentru această carte și client.
        """
        inchiriere = Inchiriere(carte, client)
        self.__repo_inchirieri.adauga_inchiriere(inchiriere)

    def returneaza_carte(self, inchiriere):
        """
        Marchează o închiriere ca returnată.
        :param inchiriere: Închirierea care se dorește a fi marcată ca returnată.
        :return: -; Închirierea este actualizată cu statusul de returnare.
        :raises: ValueError dacă închirierea nu există sau nu poate fi returnată.
        """
        inchiriere.set_returnata(True)

    def cele_mai_inchiriate_carti(self):
        """
        Obține un top al celor mai închiriate cărți.
        :return: Listă de tuple (carte, număr de închirieri) ordonată descrescător în funcție de numărul de închirieri.
        """
        statistici = {}
        for inchiriere in self.__repo_inchirieri.get_all():
            carte = inchiriere.get_carte()
            if carte not in statistici:
                statistici[carte] = 0
            statistici[carte] += inchiriere.get_nr_inchirieri()
        #return sorted(statistici.items(), key=lambda x: x[1], reverse=True)
        lista_statistici = list(statistici.items())
        quickSortRec(lista_statistici, 0, len(lista_statistici) - 1)
        return lista_statistici

    def clienti_ord_desch_numar_carti(self):
        """
        Obține un top al clienților ordonați descrescător după numărul de cărți închiriate.
        :return: Listă de tuple (client, număr de închirieri) ordonată descrescător în funcție de numărul de cărți închiriate.
        """
        statistici = {}
        for inchiriere in self.__repo_inchirieri.get_all():
            client = inchiriere.get_client()
            if client not in statistici:
                statistici[client] = 0
            statistici[client] += 1
        #return sorted(statistici.items(), key=lambda x: x[1], reverse=True)
        lista_statistici = list(statistici.items())
        lista_statistici = gnome_sort_desc(lista_statistici)
        
        return lista_statistici


    def primii_20_proc_activi(self):
        """
        Obține primii 20% dintre cei mai activi clienți în funcție de numărul de cărți închiriate.
        :return: Lista primilor 20% dintre clienții cu cele mai multe închirieri.
        :raises: ValueError dacă nu există suficiente închirieri pentru a selecta primii 20%.
        """
        clienti_ordonati = self.clienti_ord_desch_numar_carti()
        top_20_percent = int(len(clienti_ordonati) * 0.2)
        if top_20_percent == 0:
            top_20_percent = 1
        return clienti_ordonati[:top_20_percent]

    def cauta_inchiriere_dupa_carte_si_client(self, carte, client):
        """
        Caută o închiriere pe baza unei cărți și a unui client.
        :param carte: Cartea asociată închirierii.
        :param client: Clientul asociat închirierii.
        :return: Obiectul `Inchiriere` dacă există o închiriere corespunzătoare, None altfel.
        """
        for inchiriere in self.__repo_inchirieri.get_all():
            if inchiriere.get_carte() == carte and inchiriere.get_client() == client:
                return inchiriere
        return None

    def sterge_inchirieri_dupa_client(self, client):
        """
        Șterge toate închirierile asociate unui client.
        :param client: Clientul căruia îi vor fi șterse toate închirierile.
        :return: -; lista de închirieri se modifică prin eliminarea tuturor închirierilor asociate clientului.
        :raises: ValueError dacă clientul nu are închirieri în sistem.
        """
        inchirieri_de_sters = []
        for inchiriere in self.__repo_inchirieri.get_all():
            if inchiriere.get_client() == client:
                inchirieri_de_sters.append(inchiriere)

        if not inchirieri_de_sters:
            raise ValueError("Clientul nu are închirieri de șters.")
        
        for inchiriere in inchirieri_de_sters:
            self.__repo_inchirieri.sterge_inchiriere(inchiriere)


# Quick Sort 
def partition(l, left, right):
        """
        Partiționează lista pentru a selecta pivotul și a ordona elementele în funcție de pivot.
        :param l: Lista de tuple (carte, număr de închirieri) de sortat.
        :param left: Indexul de început al partitiei.
        :param right: Indexul de sfârșit al partitiei.
        :return: Indexul pivotului în lista partitiei.
        """
        pivot = l[left][1]  # Pivotul este numărul de închirieri
        i = left
        j = right
        while i != j:
            while l[j][1] <= pivot and i < j:
                j -= 1
            l[i] = l[j]
            while l[i][1] >= pivot and i < j:
                i += 1
            l[j] = l[i]
        l[i] = (l[i][0], pivot)
        return i

def quickSortRec(l, left, right):
        if left < right:
            pos = partition(l, left, right)
            quickSortRec(l, left, pos - 1)
            quickSortRec(l, pos + 1, right)



#Gnome Sort 
def gnome_sort_desc(arr):
        """
        Sortează o listă de tuple (carte, număr de închirieri) descrescător în funcție de numărul de închirieri.
        :param arr: Lista de tuple (carte, număr de închirieri) de sortat.
        :return: Lista sortată descrescător în funcție de numărul de închirieri.
        """
        index = 0
        n = len(arr)
        while index < n:
            if index == 0 or arr[index][1] <= arr[index - 1][1]:  
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
        return arr
         