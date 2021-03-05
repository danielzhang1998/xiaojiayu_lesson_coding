#include <iostream>
#include <string>

class Animal
{
public:
    std::string mouth;

    void eat();
    void sleep();
    void drool();
};

class Pig : public Animal
{
public:
    void climb();
};

class Turtle : public Animal
{
public:
    void swim();
};

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

int main()
{
    Pig pig;
    Turtle turtle;
    pig.sleep();
    pig.eat();
    pig.drool();
    pig.climb();

    std::cout << std::endl;

    turtle.sleep();
    turtle.eat();
    turtle.drool();
    turtle.swim();

    return 0;
}