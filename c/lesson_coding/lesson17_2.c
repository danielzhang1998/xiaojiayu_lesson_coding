#include <stdio.h>

//  数组初始化
int main(){
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}; //  也可以部分初始化，即初始化前 n 个 元素，如 a[10] = {1, 2, 3, 4, 5} 初始化前五个元素
    for (int i = 0; i < 10; i++){
        printf("%d\n", a[i]);
    }
    printf("%lu\n", sizeof(a)); //  打印数组所占用的空间大小
}