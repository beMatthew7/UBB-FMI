from domain.client import Client
from domain.validation_client import ValidatorClient

def test_client():
    client = Client(1, "Ion Popescu", "1234567890123")
    assert client.get_id_client() == 1
    assert client.get_nume() == "Ion Popescu"
    assert client.get_CNP() == "1234567890123"

    client.set_nume("Maria Popescu")
    assert client.get_nume() == "Maria Popescu"

    client.set_CNP("2234567890123")
    assert client.get_CNP() == "2234567890123"


def test_validare_client():
    validator = ValidatorClient()
    

    client_invalid1 = Client(1, "I", "1234567890123")
    try:
        validator.validate(client_invalid1)
        assert False 
    except ValueError:
        assert True


    client_invalid2 = Client(2, "Maria Popescu", "12345")
    try:
        validator.validate(client_invalid2)
        assert False  
    except ValueError:
        assert True


    client_invalid3 = Client(3, "George Ionescu", "1234ABC567890")
    try:
        validator.validate(client_invalid3)
        assert False  
    except ValueError:
        assert True


    client_valid = Client(4, "Ana Marin", "1234567890123")
    try:
        validator.validate(client_valid)
        assert True
    except ValueError:
        assert False  