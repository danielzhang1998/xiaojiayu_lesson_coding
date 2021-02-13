#include <stdio.h>

int main(){
    char ch;

    printf("enter your grade level here!\n");
    scanf("%c", &ch);
    switch (ch)
    {
    case 'A':
        printf("You are over 90!\n");
        break;
    case 'B':
        printf("You are between 80 to 90!\n");
        break;
    case 'C':
        printf("You are between 70 to 80!\n");
        break;
    case 'D':
        printf("You are between 60 to 70!\n");
        break;
    case 'E':
        printf("You are less than 60!\n");
        break;
    default:
        printf("Enter is wrong!\n");
        break;
    }
}