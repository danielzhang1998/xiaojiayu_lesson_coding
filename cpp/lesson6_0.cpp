#include <iostream>

void convertTemperature(double TempIn, char TypeIn);

int main(void)
{
    double TempIn;
    char TypeIn;

    std::cout
        << "请输入一个温度，输入格式为 [xx.x C] 或者 [xx.x F]" << std::endl;

    std::cin >> TempIn >> TypeIn;
    std::cin.ignore(100, '\n');
    std::cout << "\n";

    convertTemperature(TempIn, TypeIn);

    return 0;
}

void convertTemperature(double TempIn, char TypeIn)
{
    //  华氏温度 == 摄氏温度 * 9.0 / 5.0 + 32
    const unsigned short ADD_SUBTRACT = 32;
    const double RATIO = 9.0 / 5.0;

    double TempOut;
    char TypeOut;

    switch (TypeIn)
    {
    case 'C':
    case 'c':
        TempOut = TempIn * RATIO + ADD_SUBTRACT;
        TypeOut = 'F';
        TypeIn = 'C';

        break;
    case 'F':
    case 'f':
        TempOut = (TempIn - ADD_SUBTRACT) / RATIO;
        TypeIn = 'F';
        TypeOut = 'C';
        break;
    default:
        TypeOut = 'E';
        break;
    }

    if (TypeOut != 'E')
    {
        std::cout << "打印计算结果..." << std::endl;
        std::cout << TempIn << TypeIn << " = " << TempOut << TypeOut << std::endl;
    }
    else
    {
        std::cout << "输入错误!!!" << std::endl;
    }

    std::cout << "请输入任意字符结束程序!" << std::endl;
    std::cin.get();
}