#include <stdio.h>
#include <stdlib.h>

struct Node{
    int value;
    struct Node *next;
};

void insertNode(struct Node **head, int value);
void printNode(struct Node *head);
void deleteNode(struct Node **head, int value);

void insertNode(struct Node **head, int value){

    struct Node *previous;
    struct Node *current;
    struct Node *new;

    current = *head;
    previous = NULL;

    while (current != NULL && current->value < value){
        previous = current;
        current = current -> next;
    }

    new = (struct Node *)malloc(sizeof(struct Node));
    if (new == NULL){
        exit(1);
    }

    new -> value = value;
    new -> next = current;

    if (previous == NULL){
        *head = new;
    }
    else{
        previous -> next = new;
    }
}

void printNode(struct Node *head){
    struct Node *current;
    current = head;
    while (current != NULL){
        printf("%d, ", current -> value);
        current = current -> next;
    }

    putchar('\n');
}

void deleteNode(struct Node **head, int value){
    struct Node *previous;
    struct Node *current;

    current = *head;
    previous = NULL;

    while (current != NULL && current -> value != value){
        previous = current;
        current = current -> next;
    }

    if (current == NULL){
        printf("查无此值!\n");
        return;
    }
    else{
        if (previous == NULL){
            *head = current -> next;
        }
        else{
            previous -> next = current -> next;
        }
        free(current);
    }
}

int main(void){
    struct Node *head = NULL;
    int input;

    while (1){
        printf("请输入一个需要插入的整数(输入 886886886 表示结束)\n");
        scanf("%d", &input);

        if (input == 886886886){
            break;
        }
        insertNode(&head, input);
        printNode(head);
    }

    while(1){
        printf("请输入一个需要删除的整数(输入 886886886 表示结束)\n");
        scanf("%d", &input);

        if (input == 886886886){
            break;
        }
        deleteNode(&head, input);
        printNode(head);
        if (head == NULL){
            printf("列表为空,退出程序!\n");
            exit(0);
        }
    }

    return 0;
}