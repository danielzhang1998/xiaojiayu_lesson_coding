#include <stdio.h>

int main(){
    int i, num;
    _Bool flag = 1;

    printf("please enter a number here!\n");
    scanf("%d", &num);

    for (i = 2; i <= num / 2; i++){
        if (num % i == 0){
            flag = 0;
        }
    }
    if (flag == 1){
        printf("yes it is a prime number!\n");
    }else{
        printf("no it is not a prime number!\n");      
    }
    return 0;
}