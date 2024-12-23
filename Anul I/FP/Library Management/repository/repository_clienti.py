from domain.client import Client

class RepositoryClienti:
    def __init__(self):
        self.__elements = []

    def store_client(self, client: Client):
        """
        Adaugă un client la listă.
        :param client: Clientul de adăugat.
        :raises: ValueError dacă există deja un client cu același ID.
        """
        if self.find_client(client.get_id_client()) is not None:
            raise ValueError("Există deja un client cu acest ID.")
        self.__elements.append(client)

    def __find_pos(self, id: int) -> int:
        """
        Găsește poziția în listă a clientului cu ID-ul dat.
        :param id: ID-ul căutat.
        :return: Poziția în listă dacă clientul există, -1 altfel.
        """
        for index, client in enumerate(self.__elements):
            if client.get_id_client() == id:
                return index
        return -1

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

    def update_client(self, client_actualizat: Client):
        """
        Actualizează datele unui client.
        :param client_actualizat: Clientul actualizat.
        :raises: ValueError dacă nu există clientul cu ID-ul dat.
        """
        pos = self.__find_pos(client_actualizat.get_id_client())
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


class RepositoryClientiFile(RepositoryClienti):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citeste datele din fisier
        """
        with open(self.__filename, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line: 
                    continue
                try:
                    id, nume, cnp = line.split(',')
                    id = int(id)
                    client = Client(id, nume.strip(), cnp.strip())
                    super().store_client(client)
                except ValueError as e:
                    print(f"Eroare la procesarea liniei: '{line}' - {e}")

    def __save_to_file(self):
        with open(self.__filename, 'w', encoding="utf-8") as file:
            for client in self.get_all_clients():
                file.write(f"{client.get_id_client()},{client.get_nume()},{client.get_CNP()}\n")
                file.flush() 

    def store_client(self, client: Client):
        """
        Adauga client la lista si salveaza in fisier
        :param client: client de adaugat
        :return: -;
        """
        super().store_client(client)
        self.__save_to_file()

    def update_client(self, client_actualizat):
        """
        Actualizeaza client din lista si salveaza in fisier
        :param client_actualizat: client actualizat
        :return: -;
        """
        super().update_client(client_actualizat)
        self.__save_to_file()

    def delete_client(self, id: int):
        """
        Sterge client cu id-ul dat din lista si salveaza in fisier
        :param id: id-ul clientului de sters
        :return: -;
        """
        super().delete_client(id)
        self.__save_to_file()