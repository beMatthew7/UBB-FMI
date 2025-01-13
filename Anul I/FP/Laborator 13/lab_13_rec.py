
def has_common_digit(num1, num2):
    """
    Verifica daca au cel putin o cifra comuna
    :param :num1 -primul numar
    :param :num2 - al doilea numar
    :return: True daca cele doua numere au o cifra comuna
    :return: False in caz contrar
    """
    return bool(set(str(num1)) & set(str(num2)))

def is_valid_sequence(sequence):
    """
    Verifica daca secventa este valida
    :param sequence: lista de numere
    :return: True daca secventa este valida
    :return: False in caz contrar
    """
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1] or not has_common_digit(sequence[i], sequence[i + 1]):
            return False
    return True

def backRec(arr, x, index, result):
    """
    Genereaza toate subsecventele valide
    :param arr: lista de numere
    :param x: subsecventa curenta
    :param index: indexul curent
    :param result: lista de subsecvente valide
    """
    if len(x) > 2:
        result.append(x[:])
    
    for i in range(index, len(arr)):
        if not x or (arr[i] > x[-1] and has_common_digit(x[-1], arr[i])):
            x.append(arr[i])
            backRec(arr, x, i + 1, result)
            x.pop()

def find_subsequences(arr):
    """
    Găsește toate subsecvențele valide
    :param arr: Lista inițială de numere.
    :return: Lista subsecvențelor valide.
    """
    result = []
    backRec(arr, [], 0, result)
    return result

def main():
    arr = [int(x) for x in input("Introduceți lista de numere separate prin spațiu: ").split()]
    result = find_subsequences(arr)
    
    if result:
        print("Sub-secvențele valide sunt:")
        for seq in result:
            print(seq)
    else:
        print("Nu există sub-secvențe valide.")

if __name__ == "__main__":
    main()
