#include <stdio.h>

int main(){
    int a = 1;
    int b = 2;
    int c = 3;
    int d = 4;
    int e = 5;
    int *p1[5] = {&a, &b, &c, &d, &e};

    for (int i = 0; i < 5; i++){
        printf("%d\n", *p1[i]);
        printf("address: %p\n", p1[i]);
    }

    return 0;
}