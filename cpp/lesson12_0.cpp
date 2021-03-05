#include <iostream>

void changeAge(int age, int newAge);

int main(void)
{
    int age = 24;
    std::cout << "My age is " << age << std::endl;

    changeAge(age, age + 1);

    std::cout << "Now my age is " << age << std::endl;
}
//  直接传值，则 age 不会发生改变
void changeAge(int age, int newAge)
{
    age = newAge;
    std::cout << "In this, my age is " << age << std::endl;
}