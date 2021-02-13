#include <stdio.h>

int main(){
    char eat;

    printf("Did you eat yet? (Y/N)\n");
    scanf("%c", &eat);

    if (eat == 'Y'){
        printf("Ok!\n");
    }
    else{
        printf("Let's have it together!\n");
    }

    return 0;
}