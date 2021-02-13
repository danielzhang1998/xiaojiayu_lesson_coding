#include <stdio.h>

unsigned long long fact(int num);

unsigned long long fact(int num){
    unsigned long long result;

    if (num > 0){
        result = num * fact (num - 1);
    }else{
        result = 1;
    }

    return result;
}

int main(void){
    int num;
    printf("输入一个正整数:\n");
    scanf("%d", &num);

    printf("%d的阶乘是:%llu\n", num, fact(num));

    return 0;
}