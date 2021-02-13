import os, re, ssl, random, time
import urllib.request as u_request
import easygui as e
import get_url as g_url

# this is using for https://www.shutterstock.com/zh-Hant/search/kitten

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

def open_url(url):

    req = u_request.Request(url,headers = hdr)
    ssl._create_default_https_context = ssl._create_unverified_context
    html = u_request.urlopen(req).read().decode('utf-8')
    return html

def save(new_pic):
    folder = 'cat_image'
    try:
        if folder not in os.getcwd():
            os.mkdir(folder)
            os.chdir(folder)
    except FileExistsError:
        random1 = round(random.uniform(0,1),8)
        folder += str(random1)
        os.mkdir(folder)
        os.chdir(folder)

    count = 0
    for each in new_pic:
        try:
            req = u_request.Request(each, headers = hdr)
            response = u_request.urlopen(req)
            cat_image = response.read()
            filename = each.split('/')[-1]
            with open(filename,'wb') as f:
                f.write(cat_image)
            #print(each)
        except OSError as error:
            print(error)
            continue
        except ValueError as error:
            print(error)
            continue

        count += 1
        print("successful: " + str(count) + '/' + str(len(new_pic)))
    
def get_addrs(html):
    p = r'<a href=".+?"' # new
    pic = re.findall(p, html)
    new_pic = []
    for each in pic:
        #print(each)
        string1 = each.split('"')[1]    # google
        if 'data:image' not in string1 and '.js' not in string1 and '.css' not in string1 and len(string1) > 10 and 'zh-Hant/image-photo' in string1:
            string1 = g_url.transfer_url(string1)
            new_pic.append(string1)
            #print(new_pic)
    save(new_pic)
        

if __name__ == '__main__':
    url = input('enter the website address here!\n')
    for each in range(1, 11):
        new_url = url + "?page=" + str(each)
        get_addrs(open_url(new_url))
        sleep_time = round(random.uniform(0.5,2),4)
        #print(new_url)
        #print(len(new_url))
        time.sleep(sleep_time)
    e.msgbox(msg = 'Finished!')