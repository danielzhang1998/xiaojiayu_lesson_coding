#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Date{
    int year;
    int month;
    int day;
};

typedef struct Book{
    char name[40];
    char author[40];
    char publisher[40];
    struct Date date;
}BOOK, *p_book;

int main(void){

    FILE *fp;

    p_book book_for_write,book_for_read;

    book_for_write = (p_book)malloc(sizeof(BOOK));
    book_for_read = (p_book)malloc(sizeof(BOOK));

    if (book_for_write == NULL || book_for_read == NULL){
        printf("内存分配失败!\n");
        exit(EXIT_FAILURE);
    }

    strcpy(book_for_write->name, "《带你学C带你飞》");
    strcpy(book_for_write->author, "小甲鱼");
    strcpy(book_for_write->publisher, "清华大学出版社");
    book_for_write->date.year = 2017;
    book_for_write->date.month = 11;
    book_for_write->date.day = 11;

    if ((fp = fopen("file.txt", "w")) == NULL){
        printf("打开文件失败!\n");
        exit(EXIT_FAILURE);
    }

    fwrite(book_for_write, sizeof(BOOK), 1, fp);
    fclose(fp);

    if ((fp = fopen("file.txt", "r")) == NULL){
        printf("打开文件失败!\n");
        exit(EXIT_FAILURE);
    }

    fread(book_for_read, sizeof(BOOK), 1, fp);
    printf("书名: %s\n", book_for_read->name);
    printf("作者: %s\n", book_for_read->author);
    printf("出版社: %s\n", book_for_read->publisher);
    printf("出版日期: %d-%d-%d\n", book_for_read->date.year, book_for_read->date.month,book_for_read->date.day);

    fclose(fp);

    return 0;
}