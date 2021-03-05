#include "header.h"
#include <iostream>

//  编译及运行 cd "/Users/zhanghanlin/Documents/program/cpp/lesson44_0/" && g++ this.cpp that.cpp -o this && "/Users/zhanghanlin/Documents/program/cpp/lesson44_0/"this
extern unsigned short thatNum;
static bool printMe = false; //  static 表示静态作用域，即此变量仅作用于当前的文件

int main()
{

    unsigned short thisNum = 10;

    std::cout << thisNum << "! is equal to " << returnFactorial(thisNum) << std::endl;
    std::cout << thatNum << "! is equal to " << returnFactorial(thatNum) << std::endl;
    std::cout << headerNum << "! is equal to " << returnFactorial(headerNum) << std::endl;

    if (printMe)
    {
        std::cout << "I love FishC.com!" << std::endl;
    }

    return 0;
}