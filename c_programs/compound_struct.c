#include <stdio.h>

typedef struct
{
    int length;
    int width;
} rectangle;

typedef struct
{
    rectangle first;
    rectangle second;
} rectangles;

int area(rectangle rect){
    return rect.length * rect.width;
}

int area_diff(rectangles rects){
    return area(rects.second) - area(rects.first);
}


int main(){
    rectangle firstRectangle = {4, 5};
    rectangle secondRectangle = {6, 7};
    int area_one = firstRectangle.length * firstRectangle.width;
    int area_two = secondRectangle.length * secondRectangle.width;
    int area_diff = area_two - area_one;
    printf("Area difference is %d!\n", area_diff);
}

// Area difference is 22!
