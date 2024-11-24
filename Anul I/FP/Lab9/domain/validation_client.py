from domain.client import Client


class ValidatorClient:
    def validate(self, client: Client):
        """
        Validează un client dat.
        :param client: Clientul de validat.
        :return: -
        :raises: ValueError cu mesajele de eroare dacă clientul nu este valid.
        """
        errors = []

        
        if len(client.get_nume()) < 2:
            errors.append("Numele clientului trebuie să aibă cel puțin 2 caractere.")

        
        cnp = client.get_CNP()
        if not cnp.isdigit():
            errors.append("CNP-ul trebuie să conțină doar cifre.")
        if len(cnp) != 13:
            errors.append("CNP-ul trebuie să aibă exact 13 cifre.")

        
        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)
