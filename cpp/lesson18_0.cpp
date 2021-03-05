#include <iostream>
#include <string>

class Animal
{
public:
    std::string mouth;
    std::string name;

    Animal(std::string theName);

    void eat();
    void sleep();
    void drool();
};

class Pig : public Animal
{
public:
    void climb();
    Pig(std::string theName);
};

class Turtle : public Animal
{
public:
    void swim();
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

void Pig::climb()
{
    std::cout << "我是一只猪，我正在爬树!" << std::endl;
}

void Turtle::swim()
{
    std::cout << "我是一只小乌龟，我正在游泳!" << std::endl;
}

Pig::Pig(std::string theName) : Animal(theName) {}
Turtle::Turtle(std::string theName) : Animal(theName) {}

int main()
{
    Pig pig("小猪猪");
    Turtle turtle("小甲鱼");

    std::cout << "我的名字是: " << pig.name << std::endl;
    pig.sleep();
    pig.eat();
    pig.drool();
    pig.climb();

    std::cout << std::endl;

    std::cout << "我的名字是: " << turtle.name << std::endl;
    turtle.sleep();
    turtle.eat();
    turtle.drool();
    turtle.swim();

    return 0;
}