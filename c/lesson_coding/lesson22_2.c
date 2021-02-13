#include <stdio.h>

int main(){
    char a[] = "FishC";
    int b[] = {80, 92, 85, 86, 99};

    char *p = a;

    int *p2 = b;

    printf("*p = %c, *(p+1) = %c, *(p+2) = %c\n", *p, *(p+1), *(p+2));

    printf("*p = %d, *(p+1) = %d, *(p+2) = %d\n", *p2, *(p2+1), *(p2+2));   

    return 0;
}