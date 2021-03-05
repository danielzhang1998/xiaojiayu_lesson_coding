#include <iostream>

int main(void)
{
    enum weekdays //  按照先后顺序进行 0 ~ n-1 的赋值
    //  如果在 Monday 后面加上 = 10，则是从 10 开始赋值
    {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Fridat,
        Saturday,
        Sunday
    };

    weekdays today;

    today = Monday;
    std::cout << today << std::endl;

    today = Tuesday;
    std::cout << today << std::endl;

    // enum 可以搭配 switch 使用

    switch (today)
    {
    case Monday:
        std::cout << "It is the first day of this week" << std::endl;
        break;
    case Tuesday:
        std::cout << "It is the second day of this week" << std::endl;
        break;

    default:
        break;
    }
}