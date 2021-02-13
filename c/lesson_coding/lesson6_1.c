#include <stdio.h>

int main(){
    //  short 为可以携带正负符号，unsigned 为不可以携带正负符号（为了多一个位置存放数字）
    short i;
    unsigned short j;

    i = -1;
    j = 1;
    printf("%d\n", i);
    printf("%d\n", j);
    return 0;
}