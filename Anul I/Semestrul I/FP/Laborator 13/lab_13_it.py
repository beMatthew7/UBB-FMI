def has_common_digit(num1, num2):
    """
    Verifica daca au cel putin o cifra comuna
    :param :num1 -primul numar
    :param :num2 - al doilea numar
    :return: True daca cele doua numere au o cifra comuna
    :return: False in caz contrar
    """
    return bool(set(str(num1)) & set(str(num2)))



def find_subsequences_bkt_iter(arr):
    """
    Găsește toate subsecvențele valide folosind backtracking iterativ.
    :param arr: Lista inițială de numere.
    :return: Lista subsecvențelor valide.
    """
    n = len(arr)
    result = []
    x = [-1] 

    while len(x) > 0:
        choosed = False
        while not choosed and x[-1] < n - 1:
            x[-1] += 1 
            if len(x) == 1 or (arr[x[-2]] < arr[x[-1]] and has_common_digit(arr[x[-2]], arr[x[-1]])):
                choosed = True

        if choosed:
            if len(x) > 2:  
                result.append([arr[i] for i in x])
            x.append(-1)  
        else:
            x = x[:-1]  

    return result


def main():
    arr = [int(x) for x in input("Introduceți lista de numere separate prin spațiu: ").split()]
    result = find_subsequences_bkt_iter(arr)

    if result:
        print("Sub-secvențele valide sunt:")
        for seq in result:
            print(seq)
    else:
        print("Nu există sub-secvențe valide.")

if __name__ == "__main__":
    main()
