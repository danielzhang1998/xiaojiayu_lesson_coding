#include <stdio.h>

struct Book{
    char title[128];
    char author[40];
    char publisher[40];
    float price;
    unsigned int date;
    
} book; // 新建一个 struct 方式二，这种方式生成的 struct 为 全局变量

int main(void){
    struct Book new_book = {    //  新建一个 struct 方式一
        "A book", 
        "Me", 
        "Myself",
        5.84, 
        20201010 
        };
    printf("%s\n", new_book.title);
    printf("%s\n", new_book.author);
    printf("%f\n", new_book.price);
    printf("%d\n", new_book.date);
    printf("%s\n", new_book.publisher);

    printf("请输入书名:");
    scanf("%s", book.title);
    getchar();
    printf("请输入作者:");
    scanf("%s", book.author);
    getchar();
    printf("请输入售价:");
    scanf("%f", &book.price);
    getchar();
    printf("请输入出版日期:");
    scanf("%d", &book.date);
    getchar();
    printf("请输入出版社:");
    scanf("%s", book.publisher);
    getchar();

    printf("书名 %s, 作者 %s, 售价 %f, 出版日期 %d, 出版社 %s\n", book.title, book.author, book.price, book.date, book.publisher);

    return 0;
}