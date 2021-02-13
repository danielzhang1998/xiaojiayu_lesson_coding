#include <stdio.h>
#include <string.h>

int main(){
    char *str = "I love FishC.com!";
    int length;

    length = strlen(str);

    for (int i = 0; i < length; i++){
        printf("%c", str[i]);
    }
    printf("\n");
}