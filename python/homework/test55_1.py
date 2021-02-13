import urllib.request as u_req
import urllib.parse as u_parse
import re, ssl
from bs4 import BeautifulSoup

def main():
    keyword = input('enter the searching key word\n')
    ssl._create_default_https_context = ssl._create_unverified_context
    keyword = u_parse.urlencode({'word':keyword})
    response = u_req.urlopen('http://baike.baidu.com/search/word?%s' % keyword)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for each in soup.find_all(href = re.compile('item')):
        content = ''.join([each.text])
        charcter = u_parse.urlencode({'':each['href']})
        url2 = ''.join(['http://baike.baidu.com/', charcter])
        url2 = get_url(url2)
        print(url2)
        response2 = u_req.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, '-->', url2])
        print(content)

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

if __name__ == "__main__":
    main()