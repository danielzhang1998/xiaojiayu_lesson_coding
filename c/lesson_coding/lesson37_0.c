#include <stdio.h>
#include <stdlib.h>

int main(){

    unsigned long *ptr;
    ptr = (unsigned long *)malloc(sizeof(int));
    if (ptr == NULL){
        printf("分配内存失败！\n");
        exit(1);
    }

    printf("请输入一个整数:\n");
    scanf("%lu", ptr);
    printf("你输入的整数是: %lu\n", *ptr);
    free(ptr);
    printf("你输入的整数是: %lu\n", *ptr);
    return 0;
}