#include <iostream>

using namespace std;

int main(void){
    char buf[20];

    cin.ignore(7);
    cin.getline(buf, 10);   //  打印 9 个 因为字符串以 0 结尾，会自动用 0 进行占位

    cout << buf << endl;

    return 0;
}