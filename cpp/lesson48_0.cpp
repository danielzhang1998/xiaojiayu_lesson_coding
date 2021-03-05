#include <iostream>
#include <string>
#include <vector>

int main(void)
{

    std::vector<std::string> names;
    names.push_back("小甲鱼");
    names.push_back("小鱿鱼");

    for (int i = 0; i < names.size(); i++)
    {
        std::cout << names[i] << std::endl;
    }

    return 0;
}