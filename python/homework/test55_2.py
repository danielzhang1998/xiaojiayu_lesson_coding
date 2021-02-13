import urllib.request as u_req
import urllib.parse as u_parse
import re, ssl
from bs4 import BeautifulSoup

def test_url(soup):
    result = soup.find(text=re.compile("百度百科尚未收录词条"))
    if result:
        print(result[0:-1]) # 百度这个碧池在最后加了个“符号，给它去掉
        return False
    else:
        return True

def summary(soup):
    word = soup.h1.text
    # 如果存在副标题，一起打印
    if soup.h2:
        word += soup.h2.text
    # 打印标题
    print(word)
    # 打印简介
    if soup.find(class_="lemma-summary"):
        print(soup.find(class_="lemma-summary").text)   

def get_urls(soup):
    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        charcter = u_parse.urlencode({'':each['href']})
        url2 = ''.join(['http://baike.baidu.com/', charcter])
        url2 = get_url(url2)
        print(url2)
        response2 = u_req.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        yield content
        

def main():
    word = input("请输入关键词：")
    keyword = u_parse.urlencode({"word":word})
    response = u_req.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    if test_url(soup):
        summary(soup)
        
        print("下边打印相关链接：")
        each = get_urls(soup)
        while True:
            try:
                for i in range(10):
                    print(next(each))
            except StopIteration:
                break
            
            command = input("输入任意字符将继续打印，q退出程序：")
            if command == 'q':
                break
            else:
                continue

def get_url(url):
    list1 = url.split('%25')
    list1[0] = 'http://baike.baidu.com/item/'
    string2 = ''
    for each in list1:
        if each != list1[-1]:
            string2 += each + '%'
        else:
            string2 += each
    return string2

ssl._create_default_https_context = ssl._create_unverified_context
    
if __name__ == "__main__":
    main()