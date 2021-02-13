#include <stdio.h>

struct Date{
    int year;
    int month;
    int day;
};

struct Book{
    char title[128];
    char author[40];
    char publisher[40];
    float price;
    struct Date date;
    
} book = {
    "《带你学 C 带你飞》",
    "小甲鱼",
    "清华大学出版社",
    48.8,
    {2017, 11, 11}
};

int main(void){

    struct Book *pt;
    pt = &book;

    printf("书名: %s \n作者: %s \n售价: %.2f \n出版日期: %d - %d - %d \n出版社: %s\n", pt->title, pt->author, pt->price, pt->date.year, pt->date.month, pt->date.day, pt->publisher);

    return 0;
}