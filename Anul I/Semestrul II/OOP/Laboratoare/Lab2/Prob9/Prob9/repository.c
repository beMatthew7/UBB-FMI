#define _CRT_SECURE_NO_WARNINGS
#include "repository.h"
#include <string.h>
#include <stdlib.h>
#include <assert.h>

List* createList(int initialCapacity) {
	///	Creeaza o lista
	/// Parametrii: initialCapacity - capacitatea initiala a listei
    /// return: lista creata
    List* list = (List*)malloc(sizeof(List));

    list->len = 0;
    list->capacity = initialCapacity;
    list->array = (HolidayOffer*)malloc(initialCapacity * sizeof(HolidayOffer));


    return list;
}

void destroyList(List* list)
{
    /// Elibereaza memoria alocata pentru lista
    /// Parametrii: lista
    /// return: -
    if (list == NULL) return;

    for (int i = 0; i < list->len; i++)
    {
        if (list->array[i].type != NULL) {
            free(list->array[i].type);
            list->array[i].type = NULL;
        }
        if (list->array[i].destination != NULL) {
            free(list->array[i].destination);
            list->array[i].destination = NULL;
        }
        if (list->array[i].departure_date != NULL) {
            free(list->array[i].departure_date);
            list->array[i].departure_date = NULL;
        }
    }
    free(list->array);
    list->array = NULL;
    free(list);
}



void Add(HolidayOffer offer, List* l)
{
	///	Adauga oferta la lista
	/// Parametrii: offer - oferta de adaugat, l - lista de oferte
	/// return: -
   if (l->len == l->capacity)
    {
        l->capacity *= 2;
        l->array = (HolidayOffer*)realloc(l->array, l->capacity * sizeof(HolidayOffer));
    }
   l->array[l->len++] = offer;
}

void Update(HolidayOffer offer, List* l)
{
	///	Actualizeaza oferta din lista
	/// Parametrii: offer - oferta de actualizat, l - lista de oferte
    /// return: -
    for (int i = 0; i < l->len; ++i)
    {
        if (strcmp(l->array[i].type, offer.type) == 0 &&
            strcmp(l->array[i].destination, offer.destination) == 0 &&
            strcmp(l->array[i].departure_date, offer.departure_date) == 0)
        {
			free(l->array[i].type);
			free(l->array[i].destination);
			free(l->array[i].departure_date);
			l->array[i] = offer;
		}

    }
}

void Delete(HolidayOffer offer, List* l)
{
	///	Sterge oferta din lista
	/// Parametrii: offer - oferta de sters, l - lista de oferte
	/// return: -
    for (int i = 0; i < l->len; ++i)
    {
        if (strcmp(l->array[i].type, offer.type) == 0 &&
            strcmp(l->array[i].destination, offer.destination) == 0 &&
            strcmp(l->array[i].departure_date, offer.departure_date) == 0)
        {
			free(l->array[i].type);
			free(l->array[i].destination);
			free(l->array[i].departure_date);
            for (int j = i; j < l->len - 1; ++j)
            {
                l->array[j] = l->array[j + 1];
            }
            l->len--;
        }
    }
}

void addDefault(List* l)
{
	///	Adauga oferte default in lista
	/// Parametrii: lista
    /// return: -
    
	HolidayOffer* offer = createHolidayOffer("city_break", "Bucuresti", "01/01/2025", 100);
	Add(*offer, l);
	createHolidayOffer("mare", "Mamaia", "01/02/2025", 200);
	Add(*offer, l);
	createHolidayOffer("munte", "Brasov", "01/03/2025", 300);
	Add(*offer, l);
	createHolidayOffer("city_break", "Cluj", "01/04/2025", 400);
	Add(*offer, l);



}