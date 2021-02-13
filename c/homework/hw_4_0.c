#include <stdio.h>

int main(void){
    int a, b = 3;
    a = b;
    b = b * 2;
    printf("a = %d\n", a);
    printf("b = %d\n", b);
}