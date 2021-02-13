#include <stdio.h>

int main(void){

    enum Colors {red = 10, green, blue};
    enum Colors rgb;

    for (rgb = red; rgb <= blue; rgb++){
        printf("rgb is %d\n", rgb);
    }
}