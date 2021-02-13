#include <stdio.h>

typedef int INTEGER, *PRINT;

int main(void){

    INTEGER a = 520;
    PRINT b,c;

    b = &a;
    c = b;

    printf("addr of a = %p\n", c);

    return 0;
}