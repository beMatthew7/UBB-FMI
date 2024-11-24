
from domain.carte import Carte
from domain.validation import ValidatorCarte
from repository.repository import RepositoryCarti
from service.controller import ControllerCarti
from colorama import Fore, Style

def test_adauga_carte_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery")
    assert len(service.get_all()) == 1

    try:
        service.adauga_carte(1, "Alt Titlu", "Altă descriere.", "Alt Autor") 
        assert False
    except ValueError:
        assert True

def test_cauta_carte_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery")
    carte_gasita = service.cauta_carte_dupa_titlu("Micul Print")
    assert carte_gasita.get_autor() == "Antoine de Saint-Exupery"

    carte_negasita = service.cauta_carte_dupa_titlu("Inexistent")
    assert carte_negasita is None

def test_filtrare_carti_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery")
    service.adauga_carte(2, "Lupul de Mare", "Aventurile unui marinar.", "Jack London")

    carti_filtrate = service.filtreaza_dupa_autor("Jack London")
    assert len(carti_filtrate) == 1
    assert carti_filtrate[0].get_titlu() == "Lupul de Mare"
