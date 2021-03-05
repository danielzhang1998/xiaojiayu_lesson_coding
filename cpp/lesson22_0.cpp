#include <iostream>
#include <string>

class Pet
{
public:
    Pet(std::string theName);
    ~Pet();

    static int getCount();
    friend class Cat;

protected:
    std::string name;

private:
    static int count;
};

class Dog : public Pet
{
public:
    Dog(std::string theName);
};

class Cat : public Pet
{
public:
    void catch_mouse(Pet *mouse);
    Cat(std::string theName);
};

class Mouse : public Pet
{
public:
    Mouse(std::string theName);
};

int Pet::count = 0; //  做了两件事，为 count 分配内存，将 count 初始化为 0

Pet::Pet(std::string theName)
{
    name = theName;
    count += 1;

    std::cout << "一只宠物出生了, 名字叫做: " << name << std::endl;
}

Pet::~Pet()
{
    count -= 1;
    std::cout << name << " 挂了~" << std::endl;
}

int Pet::getCount()
{
    return count;
}

Dog::Dog(std::string theName) : Pet(theName)
{
}

Cat::Cat(std::string theName) : Pet(theName)
{
}

void Cat::catch_mouse(Pet *mouse)
{
    std::cout << name << " is catching " << mouse->name << " mouse" << std::endl;
}

Mouse ::Mouse(std::string theName) : Pet(theName)
{
}

int main(void)
{
    Dog dog("Spike");
    Cat cat("Tom");
    Mouse mouse("Jerry");

    cat.catch_mouse(&mouse);

    std::cout << "已经诞生了 " << Pet::getCount() << " 只宠物!" << std::endl;

    Dog dog_2("Tyke");
    std ::cout << "现在有 " << Pet::getCount() << " 只宠物" << std::endl;

    return 0;
}
