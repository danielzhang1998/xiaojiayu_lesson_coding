import urllib.request as u_request
import urllib.parse as u_parse
import json, time, random
import translate_format,translate_browser_enter
import easygui as gui

def get_result(dict):
    # get the result from the output
    string_print = 'the result is: '
    for each in dict.items():
        if each[0] == 'translateResult':
            new_list = each[1][0]
            for each_list in range(len(new_list)):
                new_dict = new_list[each_list]
                for each in new_dict.items():
                    if each[0] == 'tgt':
                        string_print += each[1]
    gui.msgbox(msg = string_print, title = 'Translate')

def data_setting(data):
    data = translate_format.change_format(translate_browser_enter.string1)
    return data


#content = input('insert what you want to translate here!\n')
while True:
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule' # the url get from the website
    data = {}
    data = data_setting(data)
    head = {}
    head = translate_browser_enter.head
    if data['i'] == None or data['i'] == '':
        gui.msgbox('The enter is null, quit the python file!')
        break
    try:
        flag = 0
        data = u_parse.urlencode(data).encode('utf-8')
    except TypeError:
        flag = 1
        break
    finally:
        if flag == 1:
            gui.msgbox('Unknown TypeError or user quit the python file!')

    request = u_request.Request(url, data, head)

    response = u_request.urlopen(url,data)
    html = response.read().decode('utf-8')
    # print(html)
    dict = json.loads(html) # transfer from string to dict type
    # print(dict)

    # get the final result
    get_result(dict)
    sleep_time = round(random.uniform(0,3),2)
    time.sleep(sleep_time)