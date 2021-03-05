#include <iostream>
#include <string>

template <class T>
class Stack
{
public: //  内联函数，直接在 class 里面写函数的方法
    Stack(unsigned int size = 100)
    {
        this->size = size;
        data = new T[size];
        sp = 0;
    }
    ~Stack()
    {
        delete[] data;
    }
    void push(T value)
    {
        data[sp++] = value;
        std::cout << "push: " << value << std::endl;
    }

    T pop()
    {
        T temp = data[--sp];
        data[sp] = -1;
        return temp;
    }
    void print()
    {
        std::cout << "Current stuck: ";
        for (int i = 0; i < sp; i++)
        {
            std::cout << data[i] << " ";
        }
        std::cout << std::endl;
    }

private:
    unsigned int size;
    unsigned int sp;
    T *data;
};

int main(void)
{
    Stack<int> intStack(100);

    intStack.push(1);
    intStack.print();

    intStack.push(2);
    intStack.print();

    intStack.push(3);
    intStack.print();

    std::cout << "pop: " << intStack.pop() << std::endl;
    intStack.print();

    std::cout << "pop: " << intStack.pop() << std::endl;
    intStack.print();

    std::cout << "pop: " << intStack.pop() << std::endl;
    intStack.print();

    return 0;
}