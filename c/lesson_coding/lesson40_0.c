#include <stdio.h>

#define PI 3.14

int main(void){
    int r;
    float s;

    printf("请输入圆的半径:\n");
    scanf("%d", &r);

    s = PI * r * r;
    printf("圆的面积是:%.2f\n", s);

    return 0;
}