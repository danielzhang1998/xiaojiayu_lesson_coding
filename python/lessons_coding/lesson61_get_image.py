import urllib.request as u_request
import re
import ssl

def open_url(url):
    header ={}
    header['User-Agent'] = 'Mozilla/5.0 (Macintosh; M1 Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    req = u_request.Request(url,headers = header)
    ssl._create_default_https_context = ssl._create_unverified_context
    html = u_request.urlopen(req).read().decode('utf-8')
    return html

def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    image_list = re.findall(p, html)

    for each in image_list:
        filename = each.split('/')[-1]
        u_request.urlretrieve(each,filename, None)

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/6251730285'
    get_img(open_url(url))