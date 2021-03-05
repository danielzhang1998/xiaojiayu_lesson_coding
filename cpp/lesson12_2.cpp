#include <iostream>

void swap(int *x, int *y);

int main(void)
{
    int x, y;

    std::cout << "请输入两个不同的值" << std::endl;
    std::cin >> x >> y;

    swap(&x, &y);

    std::cout << "调换后输出: " << x << ' ' << y << std::endl;
}

void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}