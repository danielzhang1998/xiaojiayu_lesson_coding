#include <iostream>
#include <string>

template <class T>
class Stack
{
public:
    Stack(unsigned int size = 100);
    ~Stack();
    void push(T value);
    T pop();
    void print();

private:
    unsigned int size;
    unsigned int sp;
    T *data;
};

template <class T>
Stack<T>::Stack(unsigned int size)
{
    this->size = size;
    data = new T[size];
    sp = 0;
}

template <class T>
Stack<T>::~Stack()
{
    delete[] data;
}

template <class T>
void Stack<T>::push(T value)
{
    data[sp++] = value;
    std::cout << "push: " << value << std::endl;
}

template <class T>
T Stack<T>::pop()
{
    T temp = data[--sp];
    data[sp] = -1;
    return temp;
}

template <class T>
void Stack<T>::print()
{
    std::cout << "Current stuck: ";
    for (int i = 0; i < sp; i++)
    {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;
}

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