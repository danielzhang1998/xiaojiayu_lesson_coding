#include <stdio.h>

void func();

void func(){
    extern int count;   // 表明该变量在后面被定义了
    count ++;
}

int count = 0;

int main(){
    func();
    func();
    func();

    printf("%d\n", count);

    return 0;
}