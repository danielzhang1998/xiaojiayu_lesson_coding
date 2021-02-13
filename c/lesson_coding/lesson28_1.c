#include <stdio.h>

int sum_all(int num);

int sum_all(int num){
    int sum = 0;
    for (int i = 0; i <= num; i++){
        sum += i;
    }

    return sum;
}

int main(){
    int n;

    printf("please enter the number of variable n: ");
    scanf("%d", &n);
    int sum = sum_all(n);
    printf("the result of 1 + 2 + 3 + ... + (n - 1) + n is: %d\n", sum);
}