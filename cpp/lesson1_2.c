#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    int sum = 0;
    char ch;

    printf("请输入一串整数和任意数目的空格: ");

    while( scanf("%d", &i) == 1 )
    {
            sum += i;

            while((ch=getchar()) == ' ');
            if (ch == '\n')
            {
                break;
            }

            ungetc( ch, stdin );    // 将 ch 里面的字符退回给 stdin 输入流，因为 getchar() 会多获取一个字符
    }
    
    printf("结果是: %d", sum);
    printf("\n");
    exit(0);

    return 0;
}