#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    int num, count = 0;
    int *ptr = NULL;    //  注意，这里必须初始化为 NULL 因为 realloc 只能针对 malloc 或者 calloc 创建的对象，或者指向 NULL 的指针进行操作
    //  ptr 为 NULL 时，相当于 malloc

    while (num != -1){
        printf("请输入一个整数(输入 -1 表示结束):\n");
        scanf("%d", &num);
        count ++;

        ptr = (int *)realloc(ptr, count * sizeof(int));

        if (ptr == NULL){
            exit(1);
        }

        ptr[count - 1] = num;
    }

    printf("输入的整数分辨是:\n");

    for (int i = 0; i < count; i++){
        printf("%d ", ptr[i]);
    }
    putchar('\n');

    free(ptr);

    return 0;
}