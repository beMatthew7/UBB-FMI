#define _CRT_SECURE_NO_WARNINGS
#include "service.h"
#include "validators.h"
#include <string.h>
#include "repository.h"


void addOffer(char type[], char destination[], char departure_date[], int price, List* l) 
{
	///	Adauga oferta la lista
	/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
	/// return: -

    // Valideaza type
    if (!validateType(type)) {
        return;
    }
    // Valideaza destination
    if (!validateDestination(destination)) {
        return;
    }
    // Valideaza departure date
    if (!validateDate(departure_date)) {
        return;
    }
    // Valideaza price
    if (!validatePrice(price)) {
        return;
    }

	HolidayOffer* offer = createHolidayOffer(type, destination, departure_date, price);
	if (offer == NULL)
	{
		return;
	}
	Add(*offer, l);
	destroyHolidayOffer(offer);
}

void updateOffer(char type[], char destination[], char departure_date[], float price, List* l)
{
	///	Actualizeaza oferta din lista
	/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
	/// return: -

	HolidayOffer* offer = createHolidayOffer(type, destination, departure_date, price);
	if (offer == NULL)
	{
		return;
	}
	Update(*offer, l);
	destroyHolidayOffer(offer);
}

void deleteOffer(char type[], char destination[], char departure_date[], float price, List* l)
{
	///	Sterge oferta din lista
	/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
	/// return: -

	HolidayOffer* offer = createHolidayOffer(type, destination, departure_date, price);
	if (offer == NULL)
	{
		return;
	}
	Delete(*offer, l);
	destroyHolidayOffer(offer);
}

void addDefaultOffers(List* l)
{
	///	Adauga oferte default in lista
	/// Parametrii: lista l
	/// Lista - lista de oferte
	addDefault(l);

}

void offers_d(List* l)
{
	///	Afiseaza ofertele din lista
	/// Parametrii: lista l
	/// Lista - lista de oferte
	
	for (int i = 0; i < l->len -1; ++i)
	{
		for (int j = i + 1; j < l->len; ++j)
		{
			if (l->array[i].price < l->array[j].price)
			{

				HolidayOffer aux = l->array[i];
				l->array[i] = l->array[j];
				l->array[j] = aux;
			}
			else
			{
				if (l->array[i].price == l->array[j].price)
				{
					if (strcmp(l->array[i].destination, l->array[j].destination) < 0)
					{
						HolidayOffer aux = l->array[i];
						l->array[i] = l->array[j];
						l->array[j] = aux;
					}
				}
			}
		}
	}
}

void offers_c(List* l)
{
	///	Afiseaza ofertele din lista
	/// Parametrii: lista l
	/// Lista - lista de oferte

	for (int i = 0; i < l->len - 1; ++i)
	{
		for (int j = i + 1; j < l->len; ++j)
		{
			if (l->array[i].price > l->array[j].price)
			{
				HolidayOffer aux = l->array[i];
				l->array[i] = l->array[j];
				l->array[j] = aux;
			}
			else
			{
				if (l->array[i].price == l->array[j].price)
				{
					if (strcmp(l->array[i].destination, l->array[j].destination) > 0)
					{
						HolidayOffer aux = l->array[i];
						l->array[i] = l->array[j];
						l->array[j] = aux;
					}
				}
			}
		}
	}
}

List* filtrare_lista(char criteriu[], char valoare[], int pret, List* l) {
	///	Filtreaza lista de oferte dupa un criteriu si o valoare data
	/// Parametrii: criteriu - criteriul de filtrare, valoare - valoarea de filtrare, pret - pretul de filtrare, l - lista de oferte
	/// return: lista filtrata
    List* l2 = createList(l->capacity + 1);
    for (int i = 0; i < l->len; ++i) {
        if (strcmp(criteriu, "destinatie") == 0 && strcmp(l->array[i].destination, valoare) == 0) {
            Add(l->array[i], l2);
        } else if (strcmp(criteriu, "tip") == 0 && strcmp(l->array[i].type, valoare) == 0) {
            Add(l->array[i], l2);
        } else if (strcmp(criteriu, "pret") == 0 && l->array[i].price <= pret) {
            Add(l->array[i], l2);
        }
    }
    return l2;
}
