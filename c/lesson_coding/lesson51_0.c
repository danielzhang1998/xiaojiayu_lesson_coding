#include <stdio.h>
#include <string.h>

union Test
{
    int i;
    double pi;
    char str[6];
};

int main(void){

    union Test test;

    test.i = 520;
    test.pi = 3.14;
    strcpy(test.str, "FishC");

    printf("addr of test.i: %p\n", &test.i);
    printf("addr of test.pi: %p\n", &test.pi);
    printf("addr of test.str: %p\n", &test.str);

    return 0;
}
