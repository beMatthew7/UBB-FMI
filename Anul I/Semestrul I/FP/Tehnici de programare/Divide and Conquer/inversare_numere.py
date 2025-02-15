def f(l):
    """
    Verifica daca o lista este strict crescatoare
    :param l: lista de elemente
    :return True daca lista este strict crescatoare
            False in caz contrar
    :raise ValueError daca lista este goala        
    """
    if l == None or l == []: raise ValueError()
    aux  = l[0] - 1
    for e in l:
        if (aux - e >= 0):
            return False
        aux = e
    return True    