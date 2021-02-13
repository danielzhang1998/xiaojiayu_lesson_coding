#include <stdio.h>

int main(){
    char *p1[5] = {
        "abc123",
        "abcd1234",
        "abcde12345",
        "abcdef123456",
        "abcdefg1234567"
    };

    for (int i = 0; i < 5; i++){
        printf("%s\n", p1[i]);
    }
}