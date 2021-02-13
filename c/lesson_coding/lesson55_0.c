#include <stdio.h>

int main(void){

    int value = 1;

    while (value < 1024){
        value <<= 1;    //  左移一位是乘以 2 的 一次方，左移两位是乘以 2 的二次方
        printf("value = %d\n", value);
    }
    
    putchar('\n');

    value = 1024;
    while (value > 0){
        value >>= 2;    //  右移一位是除以 2 的 一次方，右移两位是除以 2 的二次方
        printf("value = %d\n", value);
    }

    return 0;
}