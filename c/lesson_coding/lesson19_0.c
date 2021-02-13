#include <stdio.h>
#include <string.h>

int main(){
    char str[] = "I love FishC.com!";

    printf("sizeof str = %lu\n", sizeof(str));
    printf("strlen str = %lu\n", strlen(str));  //  strlen 不包含最后的结束符
}