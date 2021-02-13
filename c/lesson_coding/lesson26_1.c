#include <stdio.h>

int main(){
    char *cBooks[] = {
        "Book A",
        "Book B",
        "Book C",
        "Book D",
        "Book E",
        "Book F"
    };

    char **byFishC;
    char **jiayuloves[4];

    byFishC = &cBooks[5];
    jiayuloves[0] = &cBooks[0];
    jiayuloves[1] = &cBooks[1];
    jiayuloves[2] = &cBooks[2];
    jiayuloves[3] = &cBooks[3];

    printf("By FishC: %s\n", *byFishC);
    printf("jiayu loves:\n");

    for (int i = 0; i < 5; i++){
        printf("%s\n", *jiayuloves[i]);
    }

    return 0;
}