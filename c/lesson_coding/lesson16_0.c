#include <stdio.h>

int main(){
    int i = 5;
    while (i ++){
        if (i > 10){
            goto A;
        }
    }
A:  printf("Hello world! I am %d!\n", i);

    return 0;
}