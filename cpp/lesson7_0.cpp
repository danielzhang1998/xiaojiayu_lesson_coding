#include <iostream>

#define ITEM 10

using namespace std;
int main(void)
{
    int num[ITEM];

    cout << "请输入 10 个整型数据!\n"
         << endl;

    for (int i = 0; i < ITEM; i++)
    {
        cout << "请输入第" << i + 1 << "个数据:" << endl;
        while (!(cin >> num[i])) //  当用户输入合法时，cin >> num[i] 会返回一个非 0 的值，所以当返回值为 0，!0 即为非 0， 则会运行 while 里面的语句
        {
            cin.clear();
            cin.ignore(100, '\n');
            cout << "请输入一个合法的值!" << endl;
        }
    }

    int total = 0;
    for (int j = 0; j < ITEM; j++)
    {
        total += num[j];
    }
    cout << "总和是: " << total << endl;
    float average;
    average = (float)total / ITEM;
    cout << "平均值是: " << average << endl;
    return 0;
}