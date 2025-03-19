#include "tests.h"
#include "validators.h"
#include "repository.h"
#include "service.h"
#include <assert.h>
#include <stdio.h>

void test_validateType() {
    assert(validateType("mare") == 1);
    assert(validateType("munte") == 1);
    assert(validateType("city_break") == 1);
    assert(validateType("invalid") == 0);
    assert(validateType("") == 0);
    assert(validateType("campie") == 0);
}

void test_validateDestination() {
    assert(validateDestination("Bucuresti") == 1);
    assert(validateDestination("") == 0);
	assert(validateDestination("i") == 0);
	assert(validateDestination("Brasov") == 1);
	assert(validateDestination("Cluj") == 1);
	assert(validateDestination("Cincu") == 1);
	assert(validateDestination("Stei") == 1);
}

void test_validatePrice() {
    assert(validatePrice(100) == 1);
    assert(validatePrice(-10) == 0);
	assert(validatePrice(700) == 1);
}

void test_validateDate() {
    
    assert(validateDate("01/01/2025") == 1); 
    assert(validateDate("12/12/2023") == 1); 
    assert(validateDate("29/02/2024") == 1);  

 
    assert(validateDate("32/01/2025") == 0);  
    assert(validateDate("01/13/2025") == 0); 
    assert(validateDate("01/01/20") == 0);  
    assert(validateDate("01-01-2025") == 0);  
    assert(validateDate("00/01/2025") == 0);  
    assert(validateDate("01/00/2025") == 0);  
    assert(validateDate("01/12/2025") == 1);  
    assert(validateDate("29/02/2023") == 0);  
    assert(validateDate("31/04/2025") == 0); 
}


void test_createList()
{
   
    List* l1 = createList(5);


    assert(l1 != NULL);  
    assert(l1->len == 0);  
    assert(l1->capacity == 5);  
    assert(l1->array != NULL);  

    
    List* l2 = createList(0);

 
    assert(l2 != NULL);  
    assert(l2->len == 0);  
    assert(l2->capacity == 0);  
    
 
    List* l3 = createList(100);

    
    assert(l3 != NULL);  
    assert(l3->len == 0);  
    assert(l3->capacity == 100);  
    assert(l3->array != NULL);  



    List* l5 = createList(5);
    if (l5 != NULL) {
        free(l5->array);  
        free(l5); 
    }

    
}

void test_destroyList() {
    List* list = createList(10);
    destroyList(list);
}

void test_Add() {
    List* list = createList(1);
    HolidayOffer offer = {"city", "Bucuresti", "01/01/2025", 100};
    Add(offer, list);
    assert(list->len == 1);
    assert(strcmp(list->array[0].type, "city") == 0);
    assert(strcmp(list->array[0].destination, "Bucuresti") == 0);
    assert(strcmp(list->array[0].departure_date, "01/01/2025") == 0);
    assert(list->array[0].price == 100);

    HolidayOffer offer2 = {"sea", "Mamaia", "01/02/2025", 200};
    Add(offer2, list);
    assert(list->len == 2);
    assert(strcmp(list->array[1].type, "sea") == 0);
    assert(strcmp(list->array[1].destination, "Mamaia") == 0);
    assert(strcmp(list->array[1].departure_date, "01/02/2025") == 0);
    assert(list->array[1].price == 200);

    destroyList(list);
}

void test_Update() {
    List* list = createList(1);
    HolidayOffer offer = {"city", "Bucuresti", "01/01/2025", 100};
    Add(offer, list);
    offer.price = 150;
    Update(offer, list);
    assert(list->array[0].price == 150);

    HolidayOffer nonExisting = {"sea", "Mamaia", "01/02/2025", 200};
    Update(nonExisting, list);
    assert(list->len == 1);

    destroyList(list);
}

void test_Delete()
{
    List* l = createList(5);

    HolidayOffer offer1 = { "city_break", "Bucuresti", "01/01/2025", 100 };
    HolidayOffer offer2 = { "sea", "Mamaia", "01/06/2025", 200 };
    HolidayOffer offer3 = { "mountain", "Brasov", "01/09/2025", 150 };
    Add(offer1, l);
    Add(offer2, l);
    Add(offer3, l);

    assert(l->len == 3);
    assert(strcmp(l->array[0].destination, "Bucuresti") == 0);
    assert(strcmp(l->array[1].destination, "Mamaia") == 0);
    assert(strcmp(l->array[2].destination, "Brasov") == 0);

    Delete(offer2, l);

    assert(l->len == 2);
    assert(strcmp(l->array[0].destination, "Bucuresti") == 0);
    assert(strcmp(l->array[1].destination, "Brasov") == 0);

    HolidayOffer offerNonExistent = { "city_break", "Cluj", "01/01/2025", 120 };
    Delete(offerNonExistent, l);

    assert(l->len == 2);

    Delete(offer1, l);

    
    assert(l->len == 1);
    assert(strcmp(l->array[0].destination, "Brasov") == 0);


    Delete(offer3, l);

    assert(l->len == 0);

 
    destroyList(l);

    
}

void test_addOffer() {
    List* list = createList(1);
    HolidayOffer offer = { "city", "Bucuresti", "01/01/2025", 100 };
    Add(offer, list);
    Delete(offer, list);
    assert(list->len == 0);



    assert(list->len == 0);

    
    addOffer("city_break", "Paris", "12/08/2025", 500, list);
    assert(list->len == 1);
    assert(strcmp(list->array[0].destination, "Paris") == 0);
    


    addOffer("invalid_type", "Roma", "10/10/2025", 300, list);
    assert(list->len == 1); 

    addOffer("mare", "A", "15/07/2025", 200, list);
    assert(list->len == 1); 

    addOffer("munte", "Brasov", "15-07-2025", 250, list);
    assert(list->len == 1); 

    
    addOffer("mare", "Constanta", "01/06/2025", -100, list);
    assert(list->len == 1); 



  
    destroyList(list);
}

void test_updateOffer() {
    List* list = createList(1);
    addOffer("mare", "Bucuresti", "01/01/2025", 100, list);
    HolidayOffer offer = { "mare", "Bucuresti", "01/01/2025", 100 };
    Add(offer, list);
    updateOffer("mare", "Bucuresti", "01/01/2025", 150, list);
    offer.price = 150;
    Update(offer, list);
    assert(list->array[0].price == 150);


    updateOffer("invalid", "", "", -1, list);
    assert(list->array[0].price == 150);

    destroyList(list);
}

void test_deleteOffer() {
    List* list = createList(1);
    addOffer("city", "Bucuresti", "01/01/2025", 100, list);
    deleteOffer("city", "Bucuresti", "01/01/2025", 100, list);
    assert(list->len == 0);

    deleteOffer("sea", "Mamaia", "01/02/2025", 200, list);
    assert(list->len == 0);

    destroyList(list);
}

void test_filtrare_destinatie() {
    List* l = createList(4);
    addTestOffers(l);

    List* filtered = filtrare_lista("destinatie", "Mamaia", 0, l);


    assert(filtered->len == 1);
    assert(strcmp(filtered->array[0].destination, "Mamaia") == 0);

    destroyList(filtered);
    destroyList(l);

}
void addTestOffers(List* l) {
    HolidayOffer* offer1 = createHolidayOffer("city_break", "Bucuresti", "01/01/2025", 100);
    Add(*offer1, l);
    destroyHolidayOffer(offer1);

    HolidayOffer* offer2 = createHolidayOffer("mare", "Mamaia", "01/02/2025", 200);
    Add(*offer2, l);
    destroyHolidayOffer(offer2);

    HolidayOffer* offer3 = createHolidayOffer("munte", "Brasov", "01/03/2025", 300);
    Add(*offer3, l);
    destroyHolidayOffer(offer3);

    HolidayOffer* offer4 = createHolidayOffer("city_break", "Cluj", "01/04/2025", 400);
    Add(*offer4, l);
    destroyHolidayOffer(offer4);
}


void test_filtrare_tip() {
    List* l = createList(4);
    addTestOffers(l);

    List* filtered = filtrare_lista("tip", "city_break", 0, l);

    assert(filtered->len == 2);
    assert(strcmp(filtered->array[0].type, "city_break") == 0);
    assert(strcmp(filtered->array[1].type, "city_break") == 0);

    destroyList(filtered);
    destroyList(l);

}


void test_filtrare_pret() {
    List* l = createList(4);
    addTestOffers(l);

    List* filtered = filtrare_lista("pret", "", 150, l);


    assert(filtered->array[0].price <= 150);
    assert(filtered->array[1].price <= 150);

    destroyList(filtered);
    destroyList(l);

}
void test_offers_c() {
    List* list = createList(5);


    HolidayOffer o1 = { "mare", "Constanta", "10/06/2025", 300 };
    HolidayOffer o2 = { "city_break", "Bucuresti", "15/07/2025", 150 };
    HolidayOffer o3 = { "mare", "Mamaia", "12/06/2025", 300 };
    HolidayOffer o4 = { "munte", "Brasov", "20/07/2025", 200 };
    HolidayOffer o5 = { "city_break", "Cluj", "05/08/2025", 150 };

    Add(o1, list);
    Add(o2, list);
    Add(o3, list);
    Add(o4, list);
    Add(o5, list);

    offers_c(list);

 
    assert(list->array[0].price == 150 && strcmp(list->array[0].destination, "Bucuresti") == 0);
    assert(list->array[1].price == 150 && strcmp(list->array[1].destination, "Cluj") == 0);
    assert(list->array[2].price == 200 && strcmp(list->array[2].destination, "Brasov") == 0);
    assert(list->array[3].price == 300 && strcmp(list->array[3].destination, "Constanta") == 0);
    assert(list->array[4].price == 300 && strcmp(list->array[4].destination, "Mamaia") == 0);


    // Eliber?m memoria
    destroyList(list);
}
void test_offers_d() {
    List* list = createList(5);


    HolidayOffer o1 = { "mare", "Constanta", "10/06/2025", 300 };
    HolidayOffer o2 = { "city_break", "Bucuresti", "15/07/2025", 150 };
    HolidayOffer o3 = { "mare", "Mamaia", "12/06/2025", 300 };
    HolidayOffer o4 = { "munte", "Brasov", "20/07/2025", 200 };
    HolidayOffer o5 = { "city_break", "Cluj", "05/08/2025", 150 };

    Add(o1, list);
    Add(o2, list);
    Add(o3, list);
    Add(o4, list);
    Add(o5, list);


    offers_d(list);


    assert(list->array[0].price == 300 && strcmp(list->array[0].destination, "Mamaia") == 0);
    assert(list->array[1].price == 300 && strcmp(list->array[1].destination, "Constanta") == 0);
    assert(list->array[2].price == 200 && strcmp(list->array[2].destination, "Brasov") == 0);
    assert(list->array[3].price == 150 && strcmp(list->array[3].destination, "Cluj") == 0);
    assert(list->array[4].price == 150 && strcmp(list->array[4].destination, "Bucuresti") == 0);



    destroyList(list);
}
void test_addDefaultOffers() {
    List* list = createList(5);


    assert(list->len == 0);

 
    addDefaultOffers(list);


    assert(list->len == 4);


    assert(strcmp(list->array[0].destination, "Bucuresti") == 0);
    assert(list->array[0].price == 100);

    assert(strcmp(list->array[1].destination, "Mamaia") == 0);
    assert(list->array[1].price == 200);

    assert(strcmp(list->array[2].destination, "Brasov") == 0);
    assert(list->array[2].price == 300);

    assert(strcmp(list->array[3].destination, "Botosani") == 0);
    assert(list->array[3].price == 100);


    destroyList(list);
}


void run_all_tests() {
    test_validateType();
    test_validateDestination();
    test_validatePrice();
    test_validateDate();
    test_createList();
    test_destroyList();
    test_Add();
    test_Update();
    test_Delete();
    test_addOffer();
    test_updateOffer();
    test_deleteOffer();
    test_filtrare_destinatie();
	test_filtrare_tip();
	test_filtrare_pret();
	test_offers_c();
	test_offers_d();
    test_addDefaultOffers();    
    printf("All tests passed successfully.\n");
}
