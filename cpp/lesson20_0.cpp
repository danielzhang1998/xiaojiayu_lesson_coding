#include <iostream>
#include <string>

class Animal
{
public:
    std::string mouth;

    Animal(std::string theName);

    void eat();
    void sleep();
    void drool();
    void get_name();

private: //  将 name 保护起来，只能在 class 内部进行访问，而不能在外部进行 访问 / 修改
    std::string name;
};

class Pig : public Animal
{
public:
    void climb();
    void eat(); //  重写 eat 函数
    Pig(std::string theName);
};

class Turtle : public Animal
{
public:
    void swim();
    void eat(); //  重写 eat 函数
    Turtle(std::string theName);
};

Animal::Animal(std::string theName)
{
    name = theName;
}

void Animal::eat()
{
    std::cout << "I'm eating!" << std::endl;
}

void Animal::sleep()
{
    std::cout << "I'm sleeping! Don't bother me!" << std::endl;
}

void Animal::drool()
{
    std::cout << "I'm drooling!" << std::endl;
}

void Animal::get_name()
{
    std::cout << "我的名字是:" << name << std::endl;
}

void Pig::climb()
{
    std::cout << "我是一只猪，我正在爬树!" << std::endl;
}

void Pig::eat() //  重写 eat 函数
{
    Animal::eat(); //  调用基类的 eat 函数
    std::cout << "我正在吃潲水" << std::endl;
}

void Turtle::swim()
{
    std::cout << "我是一只小乌龟，我正在游泳!" << std::endl;
}

void Turtle::eat() //  重写 eat 函数
{
    Animal::eat(); //  调用基类的 eat 函数
    std::cout << "我正在吃乌龟饲料" << std::endl;
}

Pig::Pig(std::string theName) : Animal(theName) {}
Turtle::Turtle(std::string theName) : Animal(theName) {}

int main()
{
    Pig pig("小猪猪");
    Turtle turtle("小甲鱼");

    pig.get_name();
    pig.sleep();
    pig.eat();
    pig.drool();
    pig.climb();

    std::cout << std::endl;

    turtle.get_name();
    turtle.sleep();
    turtle.eat();
    turtle.drool();
    turtle.swim();

    std::cout << std::endl;

    return 0;
}