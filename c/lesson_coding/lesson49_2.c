#include <stdio.h>
#include <stdlib.h>

//  将 struct Date 取别名 DATE,当需要用到指针时，取别名 *PDATE
typedef struct Date{
    int year;
    int month;
    int day;
}DATE, *PDATE;

int main(void){

    PDATE date;

    date = (PDATE)malloc(sizeof(DATE));

    if (date == NULL){
        exit(1);
    }
    
    date -> year = 2017;
    date -> month = 5;
    date -> day = 15;

    printf("%d-%d-%d\n", date -> year, date -> month, date -> day);

    return 0;
}