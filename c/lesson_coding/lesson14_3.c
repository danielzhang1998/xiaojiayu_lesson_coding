#include <stdio.h>

int main(){
    int i, j;

    for ( i = 1; j <= 9; i++){
        for (j = 1; j <= i; j++){
            printf("%d * %d = %-2d\t", i, j, i * j);
        }
        printf("\n");   // 或者 putchar('\n');
    }
}