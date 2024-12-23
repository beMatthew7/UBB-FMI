class Tara:
    def __init__(self, nume, an, inflatie, unemployment_rate, populatie):
        self.__nume = nume
        self.__an = an
        self.__inflatie = inflatie
        self.__unemployment_rate = unemployment_rate
        self.__populatie = populatie

    def get_nume(self):
        return self.__nume

    def get_an(self):
        return self.__an

    def get_inflatie(self):
        return self.__inflatie
    
    def get_unemployment_rate(self):
        return self.__unemployment_rate

    def get_populatie(self):
        return self.__populatie
    
    def set_inflatie(self, inflatie):
        self.__inflatie = inflatie

    def set_unemployment_rate(self, unemployment_rate):
        self.__unemployment_rate = unemployment_rate

    def set_populatie(self, populatie):
        self.__populatie = populatie        