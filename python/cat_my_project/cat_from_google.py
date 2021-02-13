import os, re, ssl, random, time
import urllib.request as u_request
import easygui as e

def open_url(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = u_request.Request(url,headers = hdr)
    ssl._create_default_https_context = ssl._create_unverified_context
    html = u_request.urlopen(req).read().decode('utf-8')
    return html

def save(new_pic):
    folder = 'cat_graph'
    try:
        os.mkdir(folder)
    except FileExistsError:
        folder += str(round(random.uniform(0,1),8))
        os.mkdir(folder)
    os.chdir(folder)
    count = 0
    for each in new_pic:
        url = each
        try:
            response = u_request.urlopen(url)
        except OSError:
            continue
        cat_image = response.read()
        if '.png' in str(each):
            with open(str(count) + '.png','wb') as f:
                f.write(cat_image)
        else:
            with open(str(count) + '.jpg','wb') as f:
                f.write(cat_image)
        count += 1
        print("successful: " + str(count) + '/' + str(len(new_pic)))
    e.msgbox(msg = 'Finished!')
    

def get_addrs(html):
    # p = r'data-src=".+?"'   # special case
    p = r'src=".+?"'  # google
    #p = r'ImgThumbnail":".+?"'
    pic = re.findall(p, html)
    new_pic = []
    for each in pic:
        print(each)
        string1 = each.split('"')[1]    # google
        # string1 = each.split(':"')[1]
        if 'data:image' not in string1 or '.js' not in string1 or '.css' not in string1:
            new_pic.append(string1)
            #print(new_pic)
    save(new_pic)
        

if __name__ == '__main__':
    url = input('enter\n')
    get_addrs(open_url(url))
