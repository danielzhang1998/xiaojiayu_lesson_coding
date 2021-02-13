# include <stdio.h>

int square(int num);

int square(int num){
    return num * num;
}

int main(){
    int num;

    int (*fp)(int);

    printf("请输入一个整数:\n");
    scanf("%d", &num);

    fp = square;

    printf("%d * %d = %d\n", num, num, (*fp)(num));

    return 0;
}