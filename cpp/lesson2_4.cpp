#include <iostream>
#include <math.h>

using namespace std;

int main(void){

    double result = sqrt(3.0);

    cout << "对 3 开方保留小数点后 0 ~ 9 位， 结果如下:\n" << endl;

    for (int i = 0; i <= 9; i++){
        cout.precision(i);
        cout << result << endl;
    }

    cout << "当前的输出精度为: " << cout.precision() << endl;

    return 0;
}