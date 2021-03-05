#include <iostream>
#include <fstream>
struct FishOil
{
    std::string name;
    std::string uid;
    char sex;
};

void InitFishC();
bool ReadFishC();
void RecordFishC();
bool WriteFishC(FishOil *OilData);

int main()
{
    int choose;

    InitFishC();

    while (1)
    {
        std::cout << "请选择需要执行的操作: " << std::endl;
        std::cout << "1. 打印数据到屏幕" << std::endl;
        std::cout << "2. 录入数据" << std::endl;
        std::cout << "3. 退出程序" << std::endl;
        std::cin >> choose;

        switch (choose)
        {
        case 1:
            if (ReadFishC())
            {
                std::cout << "成功读取文件" << std::endl;
            }
            else
            {
                std::cout << "读取文件失败" << std::endl;
            }
            break;
        case 2:
            RecordFishC();
            break;
        case 3:
            return 0;

        default:
            break;
        }
    }

    return 0;
}

void InitFishC()
{
    FishOil OilInt = {"小甲鱼", "fishc00001", 'M'};

    if (WriteFishC(&OilInt) == false)
    {
        std::cout << "初始化失败!" << std::endl;
    }
}

bool WriteFishC(FishOil *OilData)
{
    std::fstream f("FishC.txt", std::ios::app);

    if (f.is_open())
    {
        f << OilData->name << " ";
        f << OilData->uid << " ";
        f << OilData->sex << "\n";

        f.close();
        std::cout << "数据保存成功!" << std::endl;

        return true;
    }
    else
    {
        std::cout << "文件保存失败!" << std::endl;
        return false;
    }
}

bool ReadFishC()
{
    std::string temp;
    std::fstream f("FishC.txt", std::ios::in);

    if (f.is_open())
    {
        std::cout << " 姓名 "
                  << " id "
                  << " 性别 " << std::endl;

        while (std::getline(f, temp))
        {
            std::cout << temp << std::endl;
            std::cout << std::endl;
        }

        std::cout << std::endl;

        return true;
    }
    else
    {
        return false;
    }
}

void RecordFishC()
{
    char continue_or_not, save_or_not;
    FishOil OilData;
    FishOil *pOilData;

    continue_or_not = 'Y';

    while (continue_or_not == 'Y')
    {
        std::cout << "请输入鱼C账号: ";
        std::cin >> OilData.name;
        std::cout << "请输入鱼C身份证：";
        std::cin >> OilData.uid;
        std::cout << "请输入性别：";
        std::cin >> OilData.sex;

        std::cout << "录入成功, 请问需要保存吗？（Y/N）";
        std::cin >> save_or_not;

        if (save_or_not == 'Y')
        {
            pOilData = &OilData;
            if (WriteFishC(pOilData))
            {
                std::cout << "写入文件成功" << std::endl;
            }
            else
            {
                std::cout << "写入文件失败" << std::endl;
            }
        }
        else
        {
            return;
        }

        std::cout << "是否继续录入?(Y/N)" << std::endl;
        std::cin >> continue_or_not;
    }
}