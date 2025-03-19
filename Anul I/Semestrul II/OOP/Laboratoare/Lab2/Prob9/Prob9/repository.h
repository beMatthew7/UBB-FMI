#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "holiday_offer.h"

typedef struct {
	int len;
	int capacity;
	HolidayOffer* array; //lista alocata dinamic
}List;

List* createList(int initialCapacity);
///	Creeaza o lista
/// Parametrii: initialCapacity - capacitatea initiala a listei
/// return: lista creata

void destroyList(List* list);
///	Elibereaza memoria alocata pentru lista
/// Parametrii: lista
/// return: -

void Add(HolidayOffer offer, List* l);
///	Adauga oferta la lista
/// Parametrii: offer - oferta de adaugat, l - lista de oferte
/// return: -

void Update(HolidayOffer offer, List* l);
///	Actualizeaza oferta din lista
/// Parametrii: offer - oferta de actualizat, l - lista de oferte
/// return: -

void Delete(HolidayOffer offer, List* l);	
///	Sterge oferta din lista
/// Parametrii: offer - oferta de sters, l - lista de oferte
/// return: -

void addDefault(List* l);
///	Adauga oferte default in lista
/// Parametrii: lista
/// return: -

#endif // REPOSITORY_H
