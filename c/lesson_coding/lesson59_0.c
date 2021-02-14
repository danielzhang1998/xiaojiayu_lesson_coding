#include <stdio.h>
#include <stdlib.h>

int main(void){

    FILE *fp;

    if ((fp = fopen("hello.txt", "w")) == NULL){
        printf("文件打开失败!\n");
        exit(EXIT_FAILURE);
    }

    printf("%ld\n", ftell(fp));
    fputc('F', fp); //  写入字符
    printf("%ld\n", ftell(fp));
    fputs("ishC\n", fp);    //  写入字符串
    printf("%ld\n", ftell(fp));

    rewind(fp); //  将位置指示器初始化到文件头的位置,此时输入会直接覆盖
    printf("%ld\n", ftell(fp));
    fputs("Hello world!\n", fp);

    fclose(fp);

    return 0;
}