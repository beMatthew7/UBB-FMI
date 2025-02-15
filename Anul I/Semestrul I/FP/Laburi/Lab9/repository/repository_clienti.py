from domain.client import Client

class RepositoryClienti:
    def __init__(self):
        self.__elements = []


    def find_client(self, id: int) -> Client:
        """
        Caută clientul cu ID-ul dat.
        :param id: ID-ul clientului căutat.
        :return: Obiect de tip Client dacă există clientul cu ID-ul dat, None altfel.
        """
        for client in self.__elements:
            if client.get_id_client() == id:
                return client
        return None

    def store_client(self, client: Client):
        """
        Adaugă un client la listă.
        :param client: Clientul de adăugat.
        :raises: ValueError dacă există deja un client cu același ID.
        """
        if self.find_client(client.get_id_client()) is not None:
            raise ValueError("Există deja un client cu acest ID.")
        self.__elements.append(client)

    def __find_pos__client(self, id: int) -> int:
        """
        Găsește poziția în listă a clientului cu ID-ul dat.
        :param id: ID-ul căutat.
        :return: Poziția în listă dacă clientul există, -1 altfel.
        """
        for index, client in enumerate(self.__elements):
            if client.get_id_client() == id:
                return index
        return -1

    def update_client(self, client_actualizat: Client):
        """
        Actualizează datele unui client.
        :param client_actualizat: Clientul actualizat.
        :raises: ValueError dacă nu există clientul cu ID-ul dat.
        """
        pos = self.__find_pos__client(client_actualizat.get_id_client())
        if pos == -1:
            raise ValueError("Nu există client cu acest ID.")
        self.__elements[pos] = client_actualizat

    def delete_client(self, id: int):
        """
        Șterge clientul cu ID-ul dat.
        :param id: ID-ul clientului de șters.
        :raises: ValueError dacă nu există clientul cu ID-ul dat.
        """
        pos = self.__find_pos(id)
        if pos == -1:
            raise ValueError("Nu există un client cu acest ID.")
        del self.__elements[pos]

    def get_all_clients(self) -> list:
        """
        Returnează lista tuturor clienților.
        :return: Lista de clienți.
        """
        return self.__elements

    def get_size(self) -> int:
        """
        Returnează numărul de clienți din listă.
        :return: Numărul de clienți.
        """
        return len(self.__elements)
