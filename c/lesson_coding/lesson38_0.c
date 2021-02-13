#include <stdio.h>
#include <stdlib.h>

int main(void){
    unsigned long *ptr = NULL;
    int num;

    printf("请输入待录入整数的个数:\n");
    scanf("%d", &num);

    ptr = (unsigned long *)malloc(num * sizeof(int));

    for (int i = 0; i < num; i ++){
        printf("请录入第%d 个整数:\n", i + 1);
        scanf("%lu", &ptr[i]);
    }

    printf("你录入的整数是:\n");
    for (int i = 0; i < num; i ++){
        printf("%lu ", ptr[i]);
    }

    putchar('\n');
    free(ptr);

    return 0;
}