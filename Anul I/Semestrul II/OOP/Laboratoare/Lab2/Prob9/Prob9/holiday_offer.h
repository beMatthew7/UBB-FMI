#ifndef HOLIDAY_OFFER_H
#define HOLIDAY_OFFER_H

typedef struct {
    char* type;
    char* destination;
    char* departure_date;
    int price;
} HolidayOffer;

HolidayOffer* createHolidayOffer(char* type, char* destination, char* departure_date, int price);
void destroyHolidayOffer(HolidayOffer* offer);

#endif