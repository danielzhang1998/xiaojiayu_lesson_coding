#include <iostream>

class Complex
{
public:
    Complex();
    Complex(double r, double i);
    Complex operator+(Complex &d); //  重载加号运算符, operator 表示运算符， + 为加号
    void print();

private:
    double real;
    double imag;
};

Complex::Complex()
{
    real = 0;
    imag = 0;
}

Complex::Complex(double r, double i)
{
    real = r;
    imag = i;
}

Complex Complex::operator+(Complex &d) //  重载加号运算符
{
    Complex c;

    c.real = real + d.real;
    c.imag = imag + d.imag;

    return c;
}

void Complex::print()
{
    std::cout << "(" << real << ", " << imag << "i)" << std::endl;
}

int main(void)
{
    Complex c1(3, 4), c2(5, -10), c3;

    c3 = c1 + c2; //  使用 加号运算符重载后的方法

    std::cout << "c1 = ";
    c1.print();

    std::cout << "c2 = ";
    c2.print();

    std::cout << "c3 = ";
    c3.print();

    return 0;
}