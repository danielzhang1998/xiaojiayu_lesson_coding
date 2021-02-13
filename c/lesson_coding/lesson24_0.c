#include <stdio.h>

int main(){
    int array[4][5] = {0};

    printf("sizeof int: %lu\n", sizeof(int));
    printf("array: %p\n", array);
    printf("array + 1: %p\n", array + 1);
}