class Client:
    def __init__(self, id, nume, CNP):
        self.__id = id
        self.__nume = nume
        self.__CNP = CNP

    def get_id_client(self):
        return self.__id 

    def get_nume(self):
        return self.__nume

    def set_nume(self, new_value):
        self.__nume = new_value

    def get_CNP(self):
        return self.__CNP

    def set_CNP(self, new_value):
        self.__CNP = new_value

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id

    def __str__(self):
        return ("[" + str(self.__id) + "] Client: Nume = " + self.__nume + "; CNP = " + self.__CNP)


 