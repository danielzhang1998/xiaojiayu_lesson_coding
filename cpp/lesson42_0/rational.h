// Rational.h
// Create by 小甲鱼

// 这个头文件声明了有理数类（Rational class）
// 类里边对四则运算进行重载，以实现分数运算
//  定义一个变量，当.h 文件第一次被调用时，该变量被定义，并运行 ifndef 里面的内容。当再次调用.h 文件时，因为该变量已经被定义，则不会重新运行 ifndef 里面的内容
#ifndef RATIONAL_H

#define RATIONAL_H

#include <iostream>

namespace myMath
{

    class Rational
    {
    public:
        Rational(int num, int denom); // num = 分子, denom = 分母

        Rational operator+(Rational rhs); // rhs == right hand side
        Rational operator-(Rational rhs);
        Rational operator*(Rational rhs);
        Rational operator/(Rational rhs);

    private:
        void normalize(); // 负责对分数的简化处理

        int numerator;   // 分子
        int denominator; // 分母

        friend std::ostream &operator<<(std::ostream &os, Rational f);
    };

}

#endif
