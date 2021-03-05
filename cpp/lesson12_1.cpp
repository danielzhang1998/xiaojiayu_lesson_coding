#include <iostream>

void changeAge(int *age, int newAge);

int main(void)
{
    int age = 24;
    std::cout << "My age is " << age << std::endl;

    changeAge(&age, age + 1);

    std::cout << "Now my age is " << age << std::endl;
}
//  传递指针地址，对指针的值进行改变，则原来的 age 也会发生改变
void changeAge(int *age, int newAge)
{
    *age = newAge;
    std::cout << "In this, my age is " << *age << std::endl;
}