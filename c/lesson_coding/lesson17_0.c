#include <stdio.h>

#define NUM 10

int main(){
    int s[NUM];
    int i, sum = 0;

    for(i = 0; i < 10; i++){
        printf("Enter the %i grade here!\n", i + 1);
        scanf("%d", &s[i]);
        sum += s[i];
    }

    printf("The average is: %.2f\n", (double)sum / NUM);

    return 0;
}