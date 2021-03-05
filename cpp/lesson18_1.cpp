#include <iostream>
#include <string>

class BaseClass
{
public:
    BaseClass();
    ~BaseClass();

    void doSomething();
};

class SubClass : public BaseClass
{
public:
    SubClass();
    ~SubClass();
};

BaseClass::BaseClass()
{
    std::cout << "进入基类构造器......" << std::endl;
    std::cout << "在基类构造器中执行某些语句......" << std::endl;
}

BaseClass::~BaseClass()
{
    std::cout << "进入基类析构器......" << std::endl;
    std::cout << "在基类析构器中执行某些语句......" << std::endl;
}

void BaseClass::doSomething()
{
    std::cout << "我干了某些事情......" << std::endl;
}

SubClass::SubClass()
{
    std::cout << "进入子类构造器......" << std::endl;
    std::cout << "在子类构造器中执行某些语句......" << std::endl;
}

SubClass::~SubClass()
{
    std::cout << "进入子类析构器......" << std::endl;
    std::cout << "在子类析构器中执行某些语句......" << std::endl;
}

int main(void)
{
    SubClass subclass;
    subclass.doSomething();

    std::cout << "结束了!" << std::endl;

    return 0;
}