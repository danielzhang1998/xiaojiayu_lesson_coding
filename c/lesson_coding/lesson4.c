#include <stdio.h>

// 如何定义一个常量

#define URL "http://www.fishc.com"

int main(){
    int a = 520;
    char b = 'F';
    float c = 3.14;
    double d = 3.141592653;

    printf("常量是: %s\n", URL);
    printf("鱼 C 工作室创办于 2010 年的 %d\n", a);
    printf("I love %cishC.com!\n", b);
    printf("圆周率是: %.2f\n", c);
    printf("精确到小数点后9位的圆周率是: %11.9f\n", d);
    return 0;
}