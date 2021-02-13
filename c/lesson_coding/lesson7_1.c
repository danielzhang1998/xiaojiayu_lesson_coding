#include <stdio.h>

int main(){
    char a = 'C';
    //  %d 这里会以 ASCII 码的形式输出，字符转换成数字输出
    printf("%c = %d\n", a, a);
    return 0;
}