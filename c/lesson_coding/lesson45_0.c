#include <stdio.h>
#include <stdlib.h>

struct Book{
    char title[128];
    char author[40];
    struct Book *next;
};

void getInput(struct Book *book){

    printf("请输入书名:\n");
    scanf("%s", book -> title);
    printf("请输入作者:\n");
    scanf("%s", book -> author);
}

void addBook(struct Book **library){

    struct Book *book, *temp;
    book = (struct Book *)malloc(sizeof(struct Book));
    if (book == NULL){
        exit(1);
    }

    getInput(book);

    if (*library != NULL){
        temp = *library;
        *library = book;
        book->next = temp;
    }
    else{
        *library = book;
        book->next = NULL;
    }
}

void printlibrary(struct Book *library){
    struct Book *book;
    int count = 1;

    book = library;
    while (book != NULL){
        printf("Book: %d\n", count);
        printf("书名: %s\n", book->title);
        printf("作者: %s\n", book -> author);

        book = book->next;
        count ++;
    }
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
    releaselibrary(&library);
    return 0;
}