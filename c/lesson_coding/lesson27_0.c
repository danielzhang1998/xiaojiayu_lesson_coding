#include <stdio.h>

int main(){
    int num = 520;
    const int cnum = 880;   //  const 不可修改的常量
    const int *pc =&cnum;

    printf("cnum: %d, &cnum: %p\n", cnum, &cnum);
    printf("*pc: %d, pc: %p\n\n", *pc, pc);

    printf("----------After edit-----------\n\n");

    //  不能对常量指针所指的值进行修改，但是可以对指针指向的地址进行更改
    pc = &num;
    printf("num: %d, &num: %p\n", num, &num); 
    printf("*pc: %d, pc: %p\n", *pc, pc);

    //  修改指针指向的常量后，指针的值也会发生变化
    num = 1024;
    printf("*pc: %d, pc: %p\n", *pc, pc);

    return 0;
}