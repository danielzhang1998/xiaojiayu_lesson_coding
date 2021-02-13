#include <stdio.h>

int main(){
    //  此处一定要留一个空位给 \0 表示字符串结束位置，否则会出现乱码
    //  或者 char a[] = {'F', 'i', 's', 'h', 'C', '\0'};
    char a[6] = {'F', 'i', 's', 'h', 'C', '\0'};
    printf("%s\n", a);
    printf("Hello\n");
    return 0;
}