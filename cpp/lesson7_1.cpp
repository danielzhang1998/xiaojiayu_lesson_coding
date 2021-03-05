#include <iostream>
#include <string>

int main(void)
{
    std::string str; //  定义一个字符串类型的变量
    std::cout << "请随便输入一个字符串: " << std::endl;
    std::getline(std::cin, str); //  获取一行的输入内容，并不会因为出现空格而终止获取字符
    std::cout << str << std::endl;

    return 0;
}