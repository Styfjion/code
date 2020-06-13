#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    int id;
    int rating;
    int veganFriendly;
    int price;
    int distance;
} Restaurant;

int cmp(const *p1, const *p2) {
    Restaurant * r1 = (Restaurant *)p1;
    Restaurant * r2 = (Restaurant *)p2;
    if (r1->rating != r2->rating) {
        return r2->rating - r1->rating;
    } else {
        return r2->id - r1->id;
    }
}

int isValid(Restaurant *restaurant, int veganFriendly, int maxPrice, int maxDistance) {
    if (veganFriendly == 1 && restaurant->veganFriendly != veganFriendly) {
        return 0;
    }
    if (restaurant->price <= maxPrice && restaurant->distance <=maxDistance) {
        return 1;
    }
    return 0;
}

int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize, int veganFriendly, int maxPrice, int maxDistance, int* returnSize){
    Restaurant str_restaurants[restaurantsSize];
    for (int i = 0; i < restaurantsSize; i++) {
        memcpy(str_restaurants + i, restaurants[i], sizeof(Restaurant)); 
    }
    qsort(str_restaurants, restaurantsSize, sizeof(Restaurant), cmp);
    int *result = malloc(restaurantsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < restaurantsSize; i++) {
        if (isValid(str_restaurants + i, veganFriendly, maxPrice, maxDistance)) {
            result[count++] = str_restaurants[i].id;
        }
    }
    *returnSize = count;
    return result;
}