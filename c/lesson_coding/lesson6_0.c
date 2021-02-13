#include <stdio.h>

int main(){
    printf("int = %lu\n", sizeof(int));
    printf("short int = %lu\n", sizeof(short));
    printf("long int = %lu\n", sizeof(long));
    printf("long long int = %lu\n", sizeof(long long));
    printf("char = %lu\n", sizeof(char));
    printf("_Bool = %lu\n", sizeof(_Bool));
    printf("float = %lu\n", sizeof(float));
    printf("double = %lu\n", sizeof(double));
    printf("long double = %lu\n", sizeof(long double));

    return 0;
}