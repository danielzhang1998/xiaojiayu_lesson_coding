#include <stdio.h>

int main(){
    int a;
    int *p = &a;

    printf("请输入数字!\n");
    scanf("%d", &a);
    printf("a = %d\n", a);

    printf("请输入新的数字!\n");
    scanf("%d", p);
    printf("a = %d\n", a);
    return 0;
}