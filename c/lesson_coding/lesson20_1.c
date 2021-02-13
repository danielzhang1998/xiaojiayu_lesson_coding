#include <stdio.h>

int main(){
    int a[4][5] = {{80, 92, 85, 86, 99}, 
                   {78, 65, 89, 70, 99}, 
                   {67, 78, 76, 89, 99},
                   {88, 68, 98, 90, 99}
                   };

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 5; j++){
            printf("%d", a[i][j]);
            printf("\t");
        }
        printf("\n");
    }

    //  数组的转置（翻转输出，横竖颠倒）

    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 4; j++){
            printf("%d", a[j][i]);
            printf("\t");
        }
        printf("\n");
    }
}