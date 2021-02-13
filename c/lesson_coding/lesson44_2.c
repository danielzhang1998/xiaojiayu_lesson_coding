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
};

void getInput(struct Book *book);
void printBook(struct Book *book);

void getInput(struct Book *book){
    printf("请输入书名:");
    scanf("%s", book->title);
    getchar();
    printf("请输入作者:");
    scanf("%s", book->author);
    getchar();
    printf("请输入出版社:");
    scanf("%s", book->publisher);
    getchar();
    printf("请输入售价:");
    scanf("%f", &book->price);
    getchar();
    printf("请输入出版日期:");
    scanf("%d-%d-%d", &book->date.year, &book->date.month, &book->date.day);
    getchar();
};

void printBook(struct Book *book){
    printf("书名: %s \n作者: %s \n售价: %.2f \n出版日期: %d - %d - %d \n出版社: %s\n", book->title, book->author, book->price, book->date.year, book->date.month, book->date.day, book->publisher);
}

int main(void){
    struct Book b1, b2;

    printf("请录入第一本书的信息\n");
    getInput(&b1);
    putchar('\n');
    printf("请录入第二本书的信息\n");
    getInput(&b2);
    putchar('\n');
    printf("第一本书的信息:\n");
    printBook(&b1);
    putchar('\n');
    printf("第二本书的信息:\n");
    printBook(&b2);
    return 0;
}