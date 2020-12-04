#include <stdio.h>

typedef struct{
    int i;
    int j;
} point;

int main(){
    int i = 100;
    int j = 200;

    point one = {i, j};
    point two = {i, j};

    printf("\nAddress of i = %u", &i);
    printf("\nAddress of j = %u", &j);
    printf("\nAddress of one.i = %u", &one.i);
    printf("\nAddress of one.j = %u", &one.j);
    printf("\nAddress of two.i = %u", &two.i);
    printf("\nAddress of two.j = %u", &two.j);
}
