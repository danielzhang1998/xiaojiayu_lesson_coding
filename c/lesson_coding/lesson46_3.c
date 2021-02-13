#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Book{
    char title[128];
    char author[40];
    struct Book *next;
};

struct Book *searchbook(struct Book *library, char *target);

void getInput(struct Book *book);
void printBook(struct Book *book);
void addBook(struct Book **library);
void printlibrary(struct Book *library);
void releaselibrary(struct Book **library);


void getInput(struct Book *book){

    printf("请输入书名:\n");
    scanf("%s", book -> title);
    printf("请输入作者:\n");
    scanf("%s", book -> author);
}

void addBook(struct Book **library){

    struct Book *book;
    static struct Book *tail;

    book = (struct Book *)malloc(sizeof(struct Book));
    if (book == NULL){
        exit(1);
    }

    getInput(book);

    if (*library != NULL){
        tail -> next = book;
        book -> next = NULL;
    }
    else{
        *library = book;
        book->next = NULL;
    }

    tail = book;
}

void printlibrary(struct Book *library){
    struct Book *book;
    int count = 1;

    book = library;
    while (book != NULL){
        printf("第 %d 本书:\n", count);
        printBook(book);
        book = book->next;
        count ++;
    }
}

struct Book *searchbook(struct Book *library, char *target){
    struct Book *book;

    book = library;
    while (book != NULL){
        if (!strcmp(book -> title, target) || !strcmp(book -> author, target)){
            break;
        }
        book = book -> next;
    }

    return book;
}

void printBook(struct Book *book){

    printf("书名: %s\n", book->title);
    printf("作者: %s\n", book -> author);
}

void releaselibrary(struct Book **library){
    struct Book *temp;
    while (library != NULL){
        temp = *library;
        *library = (*library) -> next;
        free(temp);
    }
}

int main(void){
    struct Book *library = NULL;
    struct Book *book;
    char input[128];
    int ch;

    addBook(&library);

    while(1){
        printf("请问是否需要录入书籍信息(Y/N):\n");
        do{
            ch = getchar();
        }while(ch != 'Y' && ch != 'N');

        if (ch == 'Y'){
            addBook(&library);
        }
        else{
            break;
        }
    }

    printf("请问是否需要打印图书信息(Y/N):\n");
    do{
        ch = getchar();
    }while(ch != 'Y' && ch != 'N');

    if (ch == 'Y'){
        printlibrary(library);
    }

    printf("请输入需要搜索的书名或作者\n");
    scanf("%s", input);
    book = searchbook(library, input);
    if (book == NULL){
        printf("查询的内容不存在!\n");
    }
    else{
        do{
            printf("已找到符合条件的图书:\n");
            printBook(book);
        }while ((book = searchbook(book -> next, input)) != NULL);
    }

    releaselibrary(&library);
    return 0;
}