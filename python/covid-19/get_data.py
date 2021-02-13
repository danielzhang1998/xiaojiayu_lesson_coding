import re, ssl
import requests
import pandas as pd

city_or_country = []
all_data = []


def open_url(url):
# encoding: utf-8
 
    headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': "_ntes_nuid=48631ba26359e3892a6d0bf6cf52b544; _ntes_nnid=73e9c0b05b63f1d4ac3467f7d86e9b88,1610523997314; _antanalysis_s_id=1610524397238; _ntes_newsapp_install=false; hb_MA-975A-DBD9471124CE_source=www.google.com"
    
    }
    f = open('testing_new.txt','w')
    ssl._create_default_https_context = ssl._create_unverified_context
    html = requests.get(url,headers=headers).text # 获取url内容
    f.write(html)
    f.close()
    return html

def get_html(url):
    html = open_url(url)
    return html

'''
def get_country_or_city_code(url):
    html = get_html(url)
    m = r'"name".+?"id".+?,'
    result = re.findall(m, html)
    for each in range(len(result)):
        final = (result[each].split('"'))
        city_or_country.append([final[3],final[7]])
    return city_or_country
'''

def get_data_all(url):
    html = get_html(url)
    m = r'"name".+?"id".+?"extData"'        # 正则表达式获取所有国家的数据
    result = re.findall(m, html)
    for each in range(len(result)):
        string1 = ''
        final = (result[each].split('"'))
        if final[42] == '':
            final[42] = 'None'
        string1 += final[3] + ', ' + final[7] + ', ' + final[11] + ', ' + final[32] + ', ' + final[34] + ', ' + final[36] + ', ' + final[38] + ', ' + final[40] + ', ' + final[42]
        if each <= 10:
            print(final)
            print(string1)
        data = string1.split(', ')
        for each in range(3, len(data)):        # 去除不必要的标点
            if ':' in data[each]:
                new_string = ''
                new_string = data[each]
                new_string = new_string.split(':')[-1]
                data[each] = new_string
            if ',' in data[each]:
                new_string = ''
                new_string = data[each]
                new_string = new_string.split(',')[0]
                data[each] = new_string  
            if '}' in data[each]:
                new_string = ''
                new_string = data[each]
                new_string = new_string.split('}')[0]
                data[each] = new_string   
            if '{' in data[each]:
                new_string = ''
                new_string = data[each]
                new_string = new_string.split('{')[-1]
                data[each] = new_string                       
        all_data.append(data)
    print(all_data)
    return all_data

def save_as_txt(all_data, title):
    f = open('covid-19_data_set.txt','w')
    for each in title:
        each = str(each).center(30,' ')        # 对齐一下，增加美观
        f.write(each)
    f.write('\n')
    for each_one in all_data:
        for each in each_one:
            each = str(each).center(30,' ')        # 对齐一下，增加美观
            f.write(each)
        f.write('\n')
    f.close()

def save_as_csv(all_data, title):
    csv = pd.DataFrame(columns=title,data=all_data)
    csv.to_csv('csv.csv',index=False,encoding='utf_8_sig')

if __name__ == "__main__":
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=322104795402'
    '''get_country_or_city_code(url)'''
    all_data = get_data_all(url)
    title = ['name','id','lastUpdateTime','confirm','suspect','heal','dead','severe','input']        # 文件表头
    enter = input('please enter the number here: 1. save as txt file 2. save as csv file\n')
    if enter.isdigit():
        if int(enter) == 1:
            save_as_txt(all_data, title)
        elif int(enter) == 2:
            save_as_csv(all_data, title)