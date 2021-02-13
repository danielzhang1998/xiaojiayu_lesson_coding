#include <stdio.h>

// to compile it,use:    gcc lesson41_0.c -O && ./a.out
inline int square(int x);

inline int square(int x){
    return x * x;
}

int main(void){
    int i = 1;

    while (i <= 100){
        printf("%d 的平方是:%d\n", i, square(i++));
    }

    return 0;
}