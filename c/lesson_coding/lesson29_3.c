#include <stdio.h>

void get_array(int b[]);

void get_array(int b[]){
    printf("sizeof b: %lu\n", sizeof(b));
}

int main(){
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};

    printf("sizeof a: %lu\n", sizeof(a));
    get_array(a);
    return 0;
}