#include <stdio.h>

int max(int x, int y);

int max(int x, int y){
    if ( x > y ){
        return x;
    }
    else{
        return y;
    }
}

int main(){
    int a, b, c;

    printf("please enter two integer here!\n");
    scanf("%d%d", &a, &b);
    c = max(a, b);
    printf("%d is larger!\n", c);

    return 0;
}