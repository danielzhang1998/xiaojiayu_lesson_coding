#include <stdio.h>

float length(int r);
float area(int r);

float length(int r){
    return (2 * 3.14 * r);
}

float area(int r){
    return (3.14 * r * r);
}

int main(){
    float l, a;
    int r = 5;
    l = length(r);
    a = area(r);
    printf("length of r = %d circle is: %.2f, area is: %.2f\n", r, l, a);
}