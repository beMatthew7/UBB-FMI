
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte
from repository.repository_carti import RepositoryCarti
from service.controller_carte import ControllerCarti
from colorama import Fore, Style

def test_adauga_carte_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery", 20)
    assert len(service.get_all_books()) == 1

    try:
        service.adauga_carte(1, "Alt Titlu", "Altă descriere.", "Alt Autor", 20) 
        assert False
    except ValueError:
        assert True

def test_cauta_carte_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery", 20)
    carte_gasita = service.cauta_carte_dupa_titlu("Micul Print")
    assert carte_gasita.get_autor() == "Antoine de Saint-Exupery"

    carte_negasita = service.cauta_carte_dupa_titlu("Inexistent")
    assert carte_negasita is None

def test_filtrare_carti_service():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    service.adauga_carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery", 20)
    service.adauga_carte(2, "Lupul de Mare", "Aventurile unui marinar.", "Jack London", 20)

    carti_filtrate = service.filtreaza_dupa_autor("Jack London")
    assert len(carti_filtrate) == 1
    assert carti_filtrate[0].get_titlu() == "Lupul de Mare"



def test_genereaza_carti_random():
    repo = RepositoryCarti()
    validator = ValidatorCarte()
    service = ControllerCarti(repo, validator)

    numar_carti = 10
    service.genereaza_carti_random(numar_carti)

    toate_carti = service.get_all_books()
    assert len(toate_carti) == numar_carti



