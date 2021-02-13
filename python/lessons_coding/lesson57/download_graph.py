import urllib.request as u_request
import os
import base64

def url_open(url):
    header ={}
    header['User-Agent'] = 'Mozilla/5.0 (Macintosh; M1 Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    req = u_request.Request(url,headers = header)
    response = u_request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]

def find_images(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append('http:' + html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    for each in img_addrs:
        print(each)

    return img_addrs

def save_images(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def download_the_graph(folder = 'graph', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/pic/'
    page_num = int(get_page(url))

    for i in range(180,200):
        string_date = '20201216-'
        string_date += str(i)
        string_date = string_date.encode('utf-8')
        str_base64 = base64.b64encode(string_date)
        page_url = url + str_base64.decode() + '#comments'
        # print(page_url)
        img_addrs = find_images(page_url)
        save_images(folder, img_addrs)

if __name__ == '__main__':
    download_the_graph()