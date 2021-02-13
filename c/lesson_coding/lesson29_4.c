#include <stdio.h>
#include <stdarg.h>

int sum(int n, ...);

int sum(int n, ...){
    int sum = 0;
    va_list vap;

    va_start(vap, n);
    for (int i = 0; i < n; i ++){
        sum += va_arg(vap, int);
    }
    va_end(vap);

    return sum;
}

int main(){
    int result;
    result = sum(3, 1, 2, 3);
    printf("result = %d\n", result);

    result = sum(5, 1, 2, 3, 4, 5);
    printf("result = %d\n", result);

    result = sum(6, 3, -1, -2, 4, 99, 100);
    printf("result = %d\n", result);
    
    return 0;
}