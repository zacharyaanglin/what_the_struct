#include <stdio.h>

typedef struct
{
    int length;
    int width;
} rectangle;


int area(rectangle rect){
    return rect.length * rect.width;
}


int main(){
    rectangle firstRectangle = {4, 5};
    rectangle secondRectangle = {6, 7};
    int area_diff = area(secondRectangle) - area(firstRectangle);
    printf("Area difference is %d!\n", area_diff);
}

// Area difference is 22!
