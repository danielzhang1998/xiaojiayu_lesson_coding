#include <stdio.h>

int main(){
    int num = 520;
    const int cnum = 520;
    int *const p = &num;

    *p = 1024;  //  指向非常量的指针常量的值可以发生改变，但是指针自身(地址)不能，如 p = &num
    printf("*p: %d\n", *p);
    printf("p: %p\n", p);

    return 0;
}