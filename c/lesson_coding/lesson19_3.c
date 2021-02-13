#include <stdio.h>
#include <string.h>

int main(){
    char str1[] = "FishC.com!";
    char str2[] = "FishC.com!";

    if (!strcmp(str1, str2)){
        printf("str1 and str2 are same!\n");
    }
    else{
        printf("str1 and str2 are not same!\n");       
    }
}