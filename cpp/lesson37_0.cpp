#include <iostream>
#include <string>

class MyClass
{
public:
    MyClass(int *p);
    ~MyClass();

    MyClass &operator=(const MyClass &rhs);
    void print();

private:
    int *ptr;
};

MyClass::MyClass(int *p)
{
    ptr = p;
}

MyClass::~MyClass()
{
    delete ptr;
}
//  a = b;
MyClass &MyClass::operator=(const MyClass &rhs)
{
    if (this != &rhs)
    {
        delete ptr;

        ptr = new int;
        *ptr = *rhs.ptr;
    }
    else
    {
        std::cout << "赋值两边为同一个对象, 不作处理" << std::endl; //  obj1 = obj1;
    }

    return *this;
}

void MyClass::print()
{
    std::cout << *ptr << std::endl;
}

int main(void)
{
    MyClass obj1(new int(1));
    MyClass obj2(new int(2));

    obj1.print();
    obj2.print();

    obj2 = obj1;

    obj1.print();
    obj2.print();

    return 0;
}