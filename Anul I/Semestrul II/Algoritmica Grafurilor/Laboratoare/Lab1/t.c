#include <stdio.h>

void afisare_menu()
{
    printf("1. Afisarea numerelor pare pana la un numar dat\n");
    printf("2. Iesire\n");
    printf("Alegeti optiunea dumneavoastra: ");
}

void nr_pare(int numere_pare[], int n)
{
    for(int i = 2; i <= n; i += 2)
    {
        numere_pare[i] = i;
    }

}


int main()
{
    while (1){
        afisare_menu();
        char optiune;
        scanf("%c", &optiune);
        if(optiune == '1')
        {
            printf("Introduceti un numar: ");
            int numar;
            scanf("%d", &numar);

            int numere_pare[numar];
            nr_pare(numere_pare, numar);
            for(int i = 2; i <= numar; i += 2)
            {
                printf("%d ", numere_pare[i]);
            }
            printf("\n");
            
        }
        else if(optiune == '2')
        {
            break;
        }
        else
        {
            printf("Optiunea nu este valida\n");
        }
    }

}
	
