#include <stdio.h>
#include "lesson32_2_a.c"
#include "lesson32_2_b.c"
#include "lesson32_2_c.c"


void a(void);
void b(void);
void c(void);

int count;

int main(void){
    a();
    b();
    c();
    b();
    c();
    a();

    printf("Total count:%d\n", count);

    return 0;
}