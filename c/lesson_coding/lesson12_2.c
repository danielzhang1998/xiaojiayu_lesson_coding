#include <stdio.h>

int main(){
    char isRain, isFree;

    printf("Free or not? (Y/N)\n");
    scanf("%c", &isFree);

    getchar();  //  用 getchar() 接收回车，因为在上面输入完毕后，会键入一个回车，需要将回车吸收掉，否则回车会传入给下一个 scanf

    printf("Rain or not? (Y/N)\n");
    scanf("%c", &isRain);

    if (isFree == 'Y'){
        if (isRain == 'Y'){
            printf("Remember to bring the umbrella!\n");
        }
    else{
        printf("it is none of your business!\n");
    }
    }
    return 0;
}