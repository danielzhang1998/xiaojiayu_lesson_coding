#include <iostream>
#include <string>

class Pet
{
public:
    Pet(std::string theName);

    void eat();
    void sleep();
    virtual void play(); //  虚方法: 该基类的派生类可以重载该方法

protected:
    std::string name;
};

class Dog : public Pet
{
public:
    void bark();
    void play();
    Dog(std::string theName);
};

class Cat : public Pet
{
public:
    void climb();
    void play();
    Cat(std::string theName);
};

Pet::Pet(std::string theName)
{
    name = theName;
}

void Pet::eat()
{
    std::cout << name << "正在吃东西!" << std::endl;
}

void Pet::sleep()
{
    std::cout << name << "正在睡大觉!" << std::endl;
}

void Pet::play()
{
    std::cout << name << "正在玩儿!" << std::endl;
}

Dog::Dog(std::string theName) : Pet(theName)
{
}

void Dog::bark()
{
    std::cout << name << "旺~旺~\n";
}

void Dog::play()
{
    Pet::play(); //  继承基类的 play 函数
    std::cout << name << "正在追赶那只该死的猫!\n";
}

Cat::Cat(std::string theName) : Pet(theName)
{
}

void Cat::climb()
{
    std::cout << name << "正在爬树!\n";
}

void Cat::play()
{
    Pet::play(); //  继承基类的 play 函数
    std::cout << name << "玩毛线球!\n";
}

int main(void)
{
    Pet *cat = new Cat("加菲猫");
    Pet *dog = new Dog("欧弟");

    cat->sleep();
    cat->eat();
    cat->play();

    dog->sleep();
    dog->eat();
    dog->play();

    delete cat;
    delete dog;

    return 0;
}
