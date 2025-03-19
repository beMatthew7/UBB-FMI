#ifndef TESTS_H
#define TESTS_H

#include "repository.h" // Ensure List type is known

void test_validateType();
void test_validateDestination();
void test_validatePrice();
void test_validateDate();
void test_createList();
void test_destroyList();
void test_Add();
void test_Update();
void test_Delete();
void test_addOffer();
void test_updateOffer();
void test_deleteOffer();
void test_filtrare_lista();
void addTestOffers(List* l);

void run_all_tests();

#endif // TESTS_H
