#include <iostream>
#include <string>

template <class T>
void swap(T &a, T &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}

int main(void)
{
    int i1 = 100;
    int i2 = 200;
    std::cout << "交换前"
              << " i1 = " << i1 << ", i2 = " << i2 << std::endl;

    swap(i1, i2);

    std::cout << "交换后"
              << " i1 = " << i1 << ", i2 = " << i2 << std::endl;

    std::string s1 = "小甲鱼";
    std::string s2 = "小鱿鱼";

    std::cout << "交换前"
              << " s1 = " << s1 << ", s2 = " << s2 << std::endl;

    swap(s1, s2);

    std::cout << "交换后"
              << " s1 = " << s1 << ", s2 = " << s2 << std::endl;

    return 0;
}