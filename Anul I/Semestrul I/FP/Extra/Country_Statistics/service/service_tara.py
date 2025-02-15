from domain.tara import Tara

class ControllerTara:
    def __init__(self, repo_tara, validator):
        """
        Initializam controllerul pentru tari
        :param repo_tara: repository-ul pentru tari
        """
        self.__repo_tara = repo_tara
        self.__validator = validator

    def adaugare_statistica(self, nume, an, inflatie, unemployment_rate, populatie):
        """
        Adaugam o tara
        :param nume: numele tarii
        :param an: anul
        :param inflatie: inflatia
        :param unemployment_rate: unemployment rate-ul
        :param populatie: populatia
        :return: None
        """
        populatie_str = f"{populatie:,}".replace(",", "__")
        
        tara = Tara(nume, an, inflatie, unemployment_rate, populatie_str)
        self.__validator.validate(tara)
        for tara in self.__repo_tara.get_all():
            if tara.get_nume() == nume and tara.get_an() == an:
                raise ValueError("Tara exista deja!")
        self.__repo_tara.store(tara)   

    def afisare_tari_cu_inflatie_mica(self, rata_inflatie):
        inflatie_suma = {}
        numar_statistici = {}
        for tara in self.__repo_tara.get_all():
            nume = tara.get_nume()
            if nume not in inflatie_suma:
                inflatie_suma[nume] = 0
                numar_statistici[nume] = 0
            inflatie_suma[nume] += tara.get_inflatie()
            numar_statistici[nume] += 1

        # Calculează rata medie a inflației
        inflatie_medie = {}
        for nume in inflatie_suma:
            inflatie_medie[nume] = inflatie_suma[nume] / numar_statistici[nume]

        # Filtrează țările care îndeplinesc condiția
        rezultat = []
        for tara in self.__repo_tara.get_all():
            nume = tara.get_nume()
            if inflatie_medie[nume] < rata_inflatie:
                # Calculează numărul de șomeri pentru țară
                numar_someri = tara.get_unemployment_rate() * int(tara.get_populatie().replace("__", "")) / 100
                rezultat.append((nume, int(numar_someri)))

        # Găsește numărul maxim de șomeri pentru fiecare țară
        rezultat_final = {}
        for nume, someri in rezultat:
            if nume not in rezultat_final or someri > rezultat_final[nume]:
                rezultat_final[nume] = someri

        # Afișează rezultatul
        for nume, someri in rezultat_final.items():
            print(f"{nume} "+ f"{someri:,}".replace(",", "__"))

            
        
            
                       


