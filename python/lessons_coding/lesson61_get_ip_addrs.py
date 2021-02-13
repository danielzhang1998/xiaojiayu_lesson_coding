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

def get_ip(html):
    p = r'((?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]))</td>\n<td>(\d+)</td>'
    iplist = re.findall(p, html)
    for each in iplist:
        string = each[0] + ':' + each[1]
        print(string)

if __name__ == '__main__':
    url = 'http://cn-proxy.com/archives/218'
    get_ip(open_url(url))