#include <iostream>
#include <string>
#include <fstream>

class StoreQuote
{
public:
    std::string quote, speaker;
    std::ofstream fileOutput;

    StoreQuote();
    ~StoreQuote();

    void inputQuote();
    void inputSpeaker();
    bool write();
};

StoreQuote::StoreQuote()
{
    fileOutput.open("testing.txt", std::ios::app);
}

StoreQuote::~StoreQuote()
{
    fileOutput.close();
}

void StoreQuote::inputQuote()
{
    std::getline(std::cin, quote);
}

void StoreQuote::inputSpeaker()
{
    std::getline(std::cin, speaker);
}

bool StoreQuote::write()
{
    if (fileOutput.is_open())
    {
        fileOutput << quote << " | " << speaker << '\n';
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    StoreQuote quote;

    std::cout << "请输入一句名言: " << std::endl;
    quote.inputQuote();
    std::cout << "请输入作者: " << std::endl;
    quote.inputSpeaker();

    if (quote.write())
    {
        std::cout << "文件写入成功!" << std::endl;
    }
    else
    {
        std::cout << "文件写入失败!" << std::endl;
        return 1;
    }

    return 0;
}