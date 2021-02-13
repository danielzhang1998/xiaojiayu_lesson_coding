#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    int *ptr1 = NULL;
    int *ptr2 = NULL;

    //  第一次申请的内存空间
    ptr1 = (int *)malloc(10 * sizeof(int));

    //  进行若干操作后发现 ptr1 申请的的内存空间竟然不够用！

    //  第二次申请的内存空间

    ptr2 = (int *)malloc(20 * sizeof(int));

    //  将 ptr1 的数据拷贝到 ptr2 中
    memcpy(ptr2, ptr1, 10);
    free(ptr1);

    //  对 ptr2 申请的内存空间进行若干操作...
    free(ptr2);
    return 0;
}