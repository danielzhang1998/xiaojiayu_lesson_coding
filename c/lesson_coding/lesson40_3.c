#include <stdio.h>

#define SQUARE(x) ((x) * (x))

int main(void){
    int x;

    printf("请输入一个整数:\n");
    scanf("%d", &x);

    printf("%d 的平方是: %d\n", x, SQUARE(x));
    printf("%d 的平方是: %d\n", x + 1, SQUARE(x + 1));

    return 0;
}