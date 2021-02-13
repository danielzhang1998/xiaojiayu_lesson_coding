#include <stdio.h>

int main(){
    int i;
    printf("How old are you?\n");
    scanf("%d", &i);
    if (i >= 18){
        printf("Over 18!\n");
    }
    return 0;
}