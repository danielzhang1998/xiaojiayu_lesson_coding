#include <iostream>

using namespace std;

int main(void){
    const int SIZE = 50;
    char buf[SIZE];

    cout << "请输入一段文本:";
    cin.read(buf, 20);

    cout << "字符串收集到的字符数为:" << cin.gcount() << endl;

    cout << "输入的文本信息是:";
    cout.write(buf, 20);
    cout << endl;

    return 0;
}