import urllib.request as u_req
from bs4 import BeautifulSoup
import ssl, re

def main():
    url = 'http://baike.baidu.com/view/284853.htm'
    ssl._create_default_https_context = ssl._create_unverified_context
    response = u_req.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for each in soup.find_all(href = re.compile('item')):
        print(each.text, '-->', ''.join(['http://baike.baidu.com', each['href']]))

main()