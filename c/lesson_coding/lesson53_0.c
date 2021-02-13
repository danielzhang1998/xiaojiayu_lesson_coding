#include <stdio.h>

typedef unsigned int UI;

int main(void){
    struct Test{
        UI a:1;
        UI b:1;
        UI c:2;
    };

    struct Test test;

    test.a = 0;
    test.b = 1;
    test.c = 2;

    printf("a = %d, b = %d, c = %d\n", test.a, test.b, test.c);
    printf("size of test = %lu\n", sizeof(test));

    return 0;
}