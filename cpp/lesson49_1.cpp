#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

template <class T>
bool cmp1(T a, T b)
{
    return a > b;
}

int main(void)
{

    std::vector<std::string> names;
    names.push_back("Daniel");
    names.push_back("Jack");
    names.push_back("Tom");
    names.push_back("Tim");
    names.push_back("Mike");
    names.push_back("Black");
    names.push_back("Brown");

    //  顺序排列

    std::sort(names.begin(), names.end()); //  排序

    std::vector<std::string>::iterator iter = names.begin();

    while (iter != names.end()) //  end() 为 names 向量的最后一个成员的下一位
    {
        std::cout << *iter++ << std::endl;
    }

    std::cout << "\n\n";

    //  倒序排列
    std::sort(names.begin(), names.end());
    std::reverse(names.begin(), names.end());

    std::vector<std::string>::iterator iter1 = names.begin();

    while (iter1 != names.end()) //  end() 为 names 向量的最后一个成员的下一位
    {
        std::cout << *iter1++ << std::endl;
    }

    return 0;
}