#include <iostream>

using namespace std;

int main(void){
    char p;
    cout << "请输入一段文本:" << endl;

    while (cin.peek() != '\n'){
        cout << (p = cin.get());
    }

    cout << endl;

    return 0;
}