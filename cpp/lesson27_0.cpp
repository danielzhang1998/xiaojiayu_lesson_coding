#include <iostream>
#include <string>
#include <stdlib.h>

//  获取最大公约数
int gcb(int a, int b)
{
    //  分子分母之间的最大公约数
    int devide_number;
    if (b == 0)
        return a;
    else
        return gcb(b, a % b);
    return devide_number;
}

//  有理数类
class Rational
{
public:
    Rational();
    Rational(int left, int right);
    //  重写加法方法
    friend Rational operator+(Rational &c, Rational &d);
    //  重写减法方法
    friend Rational operator-(Rational &c, Rational &d);
    //  重写乘法方法
    friend Rational operator*(Rational &c, Rational &d);
    //  重写除法方法
    friend Rational operator/(Rational &c, Rational &d);
    //  约分
    friend Rational get_result(Rational &result);

    friend std::ostream &operator<<(std::ostream &os, Rational c);

private:
    //  分子
    int numerator;
    //  分母
    int denominator;
};

Rational::Rational()
{
    numerator = 0;
    denominator = 0;
}

Rational::Rational(int left, int right)
{
    numerator = left;
    denominator = right;
}

Rational operator+(Rational &c, Rational &d)
{
    Rational result;
    result.denominator = c.denominator * d.denominator;
    result.numerator = c.numerator * d.denominator + d.numerator * c.denominator;
    result = get_result(result);

    return result;
}

Rational operator-(Rational &c, Rational &d)
{
    Rational result;
    result.denominator = c.denominator * d.denominator;
    result.numerator = c.numerator * d.denominator - d.numerator * c.denominator;
    result = get_result(result);

    return result;
}

Rational operator*(Rational &c, Rational &d)
{
    Rational result;
    result.denominator = c.denominator * d.denominator;
    result.numerator = c.numerator * d.numerator;
    result = get_result(result);

    return result;
}

Rational operator/(Rational &c, Rational &d)
{
    Rational result;
    result.denominator = c.denominator * d.numerator;
    result.numerator = c.numerator * d.denominator;
    result = get_result(result);

    return result;
}

Rational get_result(Rational &result)
{
    int devide_number = gcb(result.numerator, result.denominator);
    result.denominator = result.denominator / devide_number;
    result.numerator = result.numerator / devide_number;

    return result;
}

//  重写 std::cout 方法
std::ostream &operator<<(std::ostream &os, Rational c);

int main(void)
{
    Rational c1(1, 8), c2(7, 8);

    std::cout << c1 << " + " << c2 << " = " << (c1 + c2) << std::endl;

    std::cout << c1 << " - " << c2 << " = " << (c1 - c2) << std::endl;

    std::cout << c1 << " * " << c2 << " = " << (c1 * c2) << std::endl;

    std::cout << c1 << " / " << c2 << " = " << (c1 / c2) << std::endl;
}

std::ostream &operator<<(std::ostream &os, Rational c)
{
    if (c.numerator != c.denominator)
    {
        os << c.numerator << "/" << c.denominator;
    }
    else
    {
        os << "1";
    }

    return os;
}