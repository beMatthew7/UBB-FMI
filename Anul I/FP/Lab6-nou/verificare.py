
def este_an_bisect(an):
    '''
    verifica daca anul introdus este bisect
    param: an
    returneaza True daca este an bisect, Flase in caz contrar
    '''
    return (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0)

def verificare_data(data):
    '''
    verifica daca data a fost introdusa corect
    paaram: data: data introdusa de utilizator de la tastatura
    returneaza True daca data a fost introdusa corect sau Flase in caz contrar
    '''
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False
    zi = int(data[0:2])
    luna = int(data[3:5])
    an = int(data[6:])
    if(luna < 1 or luna > 12):

        return False
    if luna in [1, 3, 5, 7, 8, 10, 12]:
        if zi < 1 or zi > 31:

            return False
    
    elif luna in [4, 6, 9, 11]:
        if zi < 1 or zi > 30:

            return False
    elif luna == 2:
        if este_an_bisect(an):  
            if zi < 1 or zi > 29:
   
                return False
        else:  
            if zi < 1 or zi > 28:

                return False

    return True

def verificare_luna(luna_dorita):
    if luna_dorita < 1 or luna_dorita > 12:
        return False  
    return True 