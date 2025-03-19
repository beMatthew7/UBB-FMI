#pragma once
#include "cheltuieli.h"

typedef struct {
    int len;
    int capacity;
    cheltuiala* array; // Dynamically allocated array
} Lista;

// Initialize a new list with a given initial capacity
Lista* createList(int initialCapacity);

// Free the memory allocated for the list
void destroyList(Lista* list);
