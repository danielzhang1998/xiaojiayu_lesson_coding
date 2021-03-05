#include <iostream>

int main(void)
{

    int a = 123;
    float b = 3.14;
    char c = 'C';
    unsigned long d = 12345678;
    std::string e = "I love FishC.com!";

    std::cout << "更改前的值:" << std::endl;

    std::cout << "a 的值是: " << a << std::endl;
    std::cout << "b 的值是: " << b << std::endl;
    std::cout << "c 的值是: " << c << std::endl;
    std::cout << "d 的值是: " << d << std::endl;
    std::cout << "e 的值是: " << e << std::endl;

    std::cout << std::endl;

    std::cout << "更改后的值:" << std::endl;
    //  通过指针对原来的值进行修改
    int *aPointer = &a;
    float *bPointer = &b;
    char *cPointer = &c;
    unsigned long *dPointer = &d;
    std::string *ePointer = &e;

    *aPointer = 234;
    *bPointer = 9.99;
    *cPointer = 'Z';
    *dPointer = 87654321;
    *ePointer = "I have a pen!";

    std::cout << "a 的值是: " << a << std::endl;
    std::cout << "b 的值是: " << b << std::endl;
    std::cout << "c 的值是: " << c << std::endl;
    std::cout << "d 的值是: " << d << std::endl;
    std::cout << "e 的值是: " << e << std::endl;

    return 0;
}