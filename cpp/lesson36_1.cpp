#include <iostream>

void swap(int *x, int *y);

int main(void)
{
    int a, b;
    a = 3;
    b = 5;

    swap(&a, &b);

    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;

    return 0;
}

void swap(int *x, int *y)
{
#if 0 //  '#if 0' 是 宏指令, 类似于 /* */, 其中 0 表示永远不执行, 如果是 1 则为永远执行 
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
#endif

    *x ^= *y;
    *y ^= *x;
    *x ^= *y;
}