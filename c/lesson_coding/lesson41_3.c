#include <stdio.h>

#define TOGETHER(x, y) x ## y   //  ## 运算符被称为记号连接运算符，可以用 ## 运算符链接两个参数

int main(void){
    printf("%d\n", TOGETHER(2, 50));

    return 0;
}