#include <iostream>

int main(void)
{
    const unsigned short ITEMS = 5;

    int intArray[ITEMS] = {1, 2, 3, 4, 5};
    char charArray[ITEMS] = {'F', 'i', 's', 'h', 'C'};
    int *intPtr = intArray;
    char *charPtr = charArray;
    std::cout << "整数型数组输出: " << std::endl;

    for (int i = 0; i < ITEMS; i++)
    {
        std::cout << *intPtr << " at " << reinterpret_cast<unsigned long>(intPtr) << std::endl; //   格式化输出地址
        intPtr++;
    }

    std::cout << "字符型数组输出: " << std::endl;

    for (int i = 0; i < ITEMS; i++)
    {
        std::cout << *charPtr << " at " << reinterpret_cast<unsigned long>(charPtr) << std::endl;
        charPtr++;
    }

    return 0;
}