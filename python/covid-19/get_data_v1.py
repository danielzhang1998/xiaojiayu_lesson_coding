import re, ssl
import requests
import pandas as pd

city_or_country = []        # 所有国家/地区的疫情信息
all_data = []        # 暂时没有使用，请等待更新

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
    index1 = html.index('areaTree') # 获取所需数据部分的其实位置
    html = html[index1:] # 去除 api 开头的不需要使用到的数据
    m = r'{"today".+?"name".+?"id"'        # 正则表达式获取所有国家的数据
    result = re.findall(m, html)
    
    for each in range(len(result)):
        final = (result[each].split('"'))
        country_data_set = []
        for every in range(len(final)):
            while (':' or ',' or '}' or '{') in final[every]:        # 去除掉不必要的符号
                if ':' in final[every]:
                    new_string = ''
                    new_string = final[every]
                    new_string = new_string.split(':')[-1]
                    final[every] = new_string
                if ',' in final[every]:
                    new_string = ''
                    new_string = final[every]
                    new_string = new_string.split(',')[0]
                    final[every] = new_string  
                if '}' in final[every]:
                    new_string = ''
                    new_string = final[every]
                    new_string = new_string.split('}')[0]
                    final[every] = new_string   
                if '{' in final[every]:
                    new_string = ''
                    new_string = final[every]
                    new_string = new_string.split('{')[-1]
                    final[every] = new_string
            if final[every].isdigit() or final[every] == 'null':        # 获取治愈，死亡等数据，如果是数据或者是 null，则写入到 list 中，否则舍弃
                country_data_set.append(final[every])           
        all_data.append(country_data_set)

    n = r'"name".+?"id".+?"children"'   # 写入国家/地区名称，编号，数据更新时间
    result_2 = re.findall(n, html)
    for each in range(len(result_2)):
        string1 = result_2[each]
        new_list = string1.split('"')
        all_data[each].insert(0,new_list[3])  
        all_data[each].insert(1,new_list[7])
        all_data[each].insert(2,new_list[11])
    return all_data

def save_as_txt(all_data, title):
    f = open('covid-19_data_set.txt','w')
    for each in title:
        each = str(each).center(25,' ')        # 对齐一下，增加美观
        f.write(each)
    f.write('\n')
    for each_one in all_data:
        for each in each_one:
            each = str(each).center(25,' ')        # 对齐一下，增加美观
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
  
    title = ['name','id','lastUpdateTime','today_confirm','today_suspect','today_heal','today_dead','today_severe','today_storeConfirm','total_confirm','total_suspect','total_heal','total_dead','total_severe','total_input','newConfirm','newDead','newHeal']        # 文件表头
    enter = input('please enter the number here: 1. save as txt file 2. save as csv file\n')
    if enter.isdigit():
        if int(enter) == 1:
            save_as_txt(all_data, title)
        elif int(enter) == 2:
            save_as_csv(all_data, title)