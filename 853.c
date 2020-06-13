#include <stdlib.h>
#include "securec.h"
typedef struct {
    int pos;
    int speed;
} Car;

int cmp(const void *p1, const void *p2) {
    Car *car1 = (Car *)p1;
    Car *car2 = (Car *)p2;
    return car1->pos - car2->pos;
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) 
{
    if (positionSize == 0) {
        return 0;
    }
    Car cars[positionSize];
    for (int i = 0; i < positionSize; i++) {
        cars[i].pos = position[i];
        cars[i].speed = speed[i];
    }
    qsort(cars, positionSize, sizeof(Car), cmp);
    int count = 1;
    float time[positionSize];
    for (int i =0; i < positionSize; i++) {
        time[i] = (float)(target - cars[i].pos) / cars[i].speed;
    }
    for (int i = positionSize - 2; i > -1; i--) {
        if (time[i] > time[i + 1]) {
            count++;
        } else {
            time[i] = time[i + 1];
        }
    }
    return count;
}

int main(int argc, char const *argv[])
{
    int position[] = {19,25,16,11,23,9,18,0,10,17,3,14,12,20,5};
    int speed[] = {7,9,6,3,3,5,1,8,3,6,10,4,6,2,6};
    int target = 27;
    printf("%d", carFleet(target, position, sizeof(position)/sizeof(int), speed, sizeof(speed)/sizeof(int)));
    return 0;
}

/*
27
[19,25,16,11,23,9,18,0,10,17,3,14,12,20,5]
[7,9,6,3,3,5,1,8,3,6,10,4,6,2,6]
*/

