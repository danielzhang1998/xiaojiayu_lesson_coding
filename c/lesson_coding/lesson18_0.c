#include <stdio.h>

int main(){
    int n,i;

    printf("please enter the num of str length:\n");
    scanf("%d", &n);
    getchar();
    char a[n + 1];

    printf("please enter the str here!\n");
    for (i = 0; i < n; i++){
        scanf("%c", &a[i]);
    }

    a[n] = '\0';
    printf("The str you enter is: %s\n", a);

    return 0;
}