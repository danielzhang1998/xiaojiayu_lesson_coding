#include <stdio.h>

int main(void){
    int i = 100;
    {
        int i = 110;
        {
            int i = 120;
            printf("i = %d\n", i);
        }
        {
            //  此处已经超出了 int i = 123 的作用域 ，但是依然在 i = 110 的作用域中
            printf("i = %d\n", i); 
            int i = 130;
            printf("i = %d\n", i);            
        }
        printf("i = %d\n", i);
    }
    printf("i = %d\n", i);

    return 0;
}