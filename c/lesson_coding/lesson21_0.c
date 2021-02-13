#include <stdio.h>

int main(){
    char a = 'F';
    int f = 123;

    char *pa = &a;
    int *pb = &f;

    printf("a = %c\n", *pa);
    printf("f = %d\n", *pb);

    printf("address of a is %p\n", pa);
    printf("address of f is %p\n", pb);

    *pa = 'C';
    *pb += 1;

    printf("now, a = %c\n", *pa);
    printf("now, f = %d\n", *pb);

    printf("now address of a is %p\n", pa);
    printf("now address of f is %p\n", pb);
}