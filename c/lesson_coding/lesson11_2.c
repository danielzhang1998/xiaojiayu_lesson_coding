#include <stdio.h>

int main(){
    int i;
    while (3 > 2){
        printf("What is your grade?\n");
        scanf("%d", &i);
        if (i >= 90){
            printf("Level A!\n");
        }
        else if (i >= 80 && i < 90){
            printf("Level B!\n");
        }
        else if (i >= 70 && i < 80){
            printf("Level C!\n");
        }
        else if (i >= 60 && i < 70){
            printf("Level D!\n");
        }
        else if (i < 60){
            printf("Level E!\n");
        }    
    }
    return 0;
}