#include <stdio.h>

int main(){
    int num = 520;
    const int cnum = 880;
    const int *const p = &num;  // 指向常量的指针常量本身不能被修改，值也不能被修改， 如 p = &cnum 和 *p = 1024
    const int * const *pp = &p;

    printf("pp: %p, &p: %p\n", pp, &p);
    printf("*pp: %p, p: %p, &num: %p\n", *pp, p, &num);
    printf("**pp: %d, *p: %d, num: %d\n", **pp, *p, num);

    return 0;
}