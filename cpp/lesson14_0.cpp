#include <iostream>

#define FULL_GAS 85

class Car
{
public:
    std::string color;
    std::string engine;
    int gas_tank;
    unsigned int wheel;

    void setColor(std::string col);
    void setEngine(std::string eng);
    void setWheel(unsigned int whe);
    void fill_tank(int liter);
    int running(void);
    void warning(void);
    void tank_fill_finished_warning(void);
};

void Car::setColor(std::string col)
{
    color = col;
}

void Car::setEngine(std::string eng)
{
    engine = eng;
}

void Car::setWheel(unsigned int whe)
{
    wheel = whe;
}

void Car::fill_tank(int liter)
{
    gas_tank += liter;
}

int Car::running(void)
{
    std::cout << "我正在以 120 的时速往前移动..." << std::endl;
    gas_tank--;
    std::cout << "当前还剩" << 100 * gas_tank / FULL_GAS << "%"
              << "油量!" << std::endl;

    return gas_tank;
}

void Car::warning(void)
{
    std::cout << "WARNING!"
              << "还剩" << 100 * gas_tank / FULL_GAS << "%"
              << "油量!" << std::endl;
}

void Car::tank_fill_finished_warning(void)
{
    std::cout << "油已经加满了，剩余油量: " << gas_tank << std::endl;
}

int main(void)
{
    char choose;
    Car mycar;

    mycar.setColor("WHITE");
    mycar.setEngine("V8");
    mycar.setWheel(4);

    mycar.gas_tank = FULL_GAS;

    int run = mycar.running();

    while (run)
    {
        run = mycar.running();
        if (run < 10 && run != 0)
        {
            mycar.warning();
            std::cout << "请问是否需要加满油再行驶?(Y/N)" << std::endl;
            std::cin >> choose;
            if ('Y' == choose || 'y' == choose)
            {
                mycar.fill_tank(FULL_GAS - mycar.gas_tank);
                mycar.tank_fill_finished_warning();
            }
        }
    }

    std::cout << "油量不足，即将熄火" << std::endl;
    return 0;
}