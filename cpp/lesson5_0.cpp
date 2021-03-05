#include <iostream>
int main(void)
{
    char answer;
    std::cout << "A question here [Y/N]"
              << "\n";
    std::cin >> answer;

    switch (answer)
    {
    case 'Y':
    case 'y':
        std::cout << "warning"
                  << "\n";
        break;
    case 'N':
    case 'n':
        std::cout << "Yes you are right"
                  << "\n";
        break;
    default:
        std::cout << "Try again!"
                  << "\n";
        break;
    }
    std::cin.ignore(100, '\n'); //  忽略 100 个字符，直到遇到回车停止忽略
    std::cout << "输入任意字符结束程序!"
              << "\n";
    std::cin.get();
    return 0;
}