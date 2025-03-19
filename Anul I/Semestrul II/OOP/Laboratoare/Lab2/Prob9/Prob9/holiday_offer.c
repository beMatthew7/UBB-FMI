#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "holiday_offer.h"

HolidayOffer* createHolidayOffer(char* type, char* destination, char* departure_date, int price)
{
	HolidayOffer* offer = (HolidayOffer*)malloc(sizeof(HolidayOffer));
	if (offer == NULL)
	{
		return NULL;
	}
	offer->type = (char*)malloc(strlen(type) + 1);
	if (offer->type == NULL)
	{
		free(offer);
		return NULL;
	}
	strcpy(offer->type, type);

	offer->destination = (char*)malloc(strlen(destination) + 1);
	if (offer->destination == NULL)
	{
		free(offer->type);
		free(offer);
		return NULL;
	}

	strcpy(offer->destination, destination);

	offer->departure_date = (char*)malloc(strlen(departure_date) + 1);
	if (offer->departure_date == NULL)
	{
		free(offer->destination);
		free(offer->type);
		free(offer);
		return NULL;
	}

	strcpy(offer->departure_date, departure_date);
	offer->price = price;
	return offer;

}

void destroyHolidayOffer(HolidayOffer* offer)
{
	if (offer == NULL)
	{
		return;
	}
	free(offer->type);
	free(offer->destination);
	free(offer->departure_date);
	free(offer);
}
