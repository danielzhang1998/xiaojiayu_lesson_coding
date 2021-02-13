#include <stdio.h>

int main(){
    int count = 0;
    printf("please enter the letters here!\n");
    while (getchar() != '\n'){
        count = count + 1;
    }
    printf("you totally insert %d letter(s)!", count);
    return 0;
}