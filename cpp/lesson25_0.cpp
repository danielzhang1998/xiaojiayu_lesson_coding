#include <iostream>

using namespace std;

class animal
{
public:
    void sleep()
    {
        cout << "animal sleep" << endl;
    }
    virtual void breathe()
    {
        cout << "animal breathe" << endl;
    }
};

class fish : public animal
{
public:
    void breathe()
    {
        cout << "fish bubble" << endl;
    }
};

class sheep : public animal
{
};

int main()
{
    fish fh;
    animal *pAn = &fh; // 隐式类型转换
    pAn->breathe();

    animal *sp = new sheep();
    sp->breathe();
}