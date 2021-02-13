#include <stdio.h>
#include <string.h>

int main(){
    char str1[50];
    char str2[50];

    strcpy(str1, "I love");
    strcpy(str2, "FishC.com!");

    strcat(str1, " ");
    strcat(str1, str2);

    printf("str1: %s\n", str1);

    return 0;
}