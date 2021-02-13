#include <stdio.h>

int main(){
    char str[] = "I love FishC.com!";
    char *p = str;
    int count = 0;

    while (*p++ != '\0'){
        count ++;
    }

    printf("total length: %d\n", count);

    return 0;
}