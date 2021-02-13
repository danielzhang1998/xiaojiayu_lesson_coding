#include <stdio.h>

void func();

int a, b = 520;

void func(){
    int b;

    a = 880;
    b = 120;

    printf("In function, a = %d, b = %d\n", a, b);
}

int main(){

    printf("In main, a = %d, b = %d\n", a, b);
    func();
    printf("In main, a = %d, b = %d\n", a, b);

    return 0;
}