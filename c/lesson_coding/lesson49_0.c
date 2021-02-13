#include <stdio.h>

//  为现有的类型创建别名,给 int 取别名为 integer
typedef unsigned int integer;

int main(){

    integer a;
    int b;

    a = -1;
    b = a;

    printf("a is %d\n", a);
    printf("b is %d\n", b);
    printf("size of a = %lu\n", sizeof(a));

    return 0;
}