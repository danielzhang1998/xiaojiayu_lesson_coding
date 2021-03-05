#include <iostream>
#include <string>
#include <vector>

int main(void)
{

    std::vector<std::string> names;
    names.push_back("小甲鱼");
    names.push_back("小鱿鱼");
    names.push_back("小鲤鱼");
    names.push_back("小鲫鱼");
    names.push_back("小鲨鱼");

    std::vector<std::string>::iterator iter = names.begin();

    while (iter != names.end()) //  end() 为 names 向量的最后一个成员的下一位
    {
        std::cout << *iter++ << std::endl;
    }

    return 0;
}