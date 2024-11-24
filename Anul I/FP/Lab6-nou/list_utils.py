

def add_to_list(lst: list, elem) -> None:
    """
    Adaugă elementul elem la lista lst.
    
    :param lst: lista în care se adaugă.
    :param elem: obiectul care se adaugă în lista.
    :return: -; lista dată se modifică prin adăugarea obiectului elem
                la finalul listei.
    """
    lst.append(elem)


def copy_list_of_lists(lst) -> list:
    """
    Creeaza o copie a unei liste de liste
    :param lst: lista de liste
    :return: o noua lista care contine noi elemente (liste) cu aceleasi valori
            ca si cele din lista initiala
            postconditii: id(lst) != id(lista returnata), oricare i, i = 0..len(lst)-1
                          id(lst[i]) != id(lista_returnata[i])
    """
    new_list = []
    for sublist in lst:
        new_sublist = []
        for item in sublist:
            new_sublist.append(item)
        new_list.append(new_sublist)
    return new_list
