#include <stdio.h>
#include <string.h>

int main(){
    char str1[] = "To be or not to be";
    char str2[40];

    strncpy(str2, str1, 5); //  复制 str1 的前五个元素到 str2
    str2[5] = '\0';     //  一定要添加一个换行符, strncpy 在拷贝结束后不会自行添加结束符

    printf("str2: %s\n", str2);

    return 0;
}