def transfer_url(string_url):
    array1 = string_url.split('/')
    string_url = 'https://image.shutterstock.com/image-photo/' + array1[-1]
    array2 = string_url.split('-')
    array2.insert(-1,'260nw')
    string_url_new = ''
    for each in range(len(array2)):
        if each != len(array2) - 1:
            string_url_new += array2[each] + '-'
        else:
            string_url_new += array2[each]
    string_url_new += '.jpg'
    return string_url_new
    