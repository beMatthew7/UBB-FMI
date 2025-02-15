class Produs:
    def __init__(self, id, denumire, pret):
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret

    def get_id(self):
        return self.__id

    def get_denumire(self):
        return self.__denumire

    def get_pret(self):
        return self.__pret

    def set_denumire(self, new_value):
        self.__denumire = new_value

    def set_pret(self, new_value):
        self.__pret = new_value

    def __eq__(self, other):
        return self.__id == other.__id
    
    def __str__(self):
        return (f"Produs:" + " " + f"{self.__id}" + " " + f"{self.__denumire}" + " " + f"{self.__pret}")         