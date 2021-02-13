from os import name
import easygui as g
import urllib.request as u_req
# get the cat picture from http://placekitten.com

def main():
    msg = 'enter the cat size'
    title = 'Cat download'
    fieldNames = ['width:', 'height:']
    fieldValues = []
    size = width, height = 400, 600
    fieldValues = g.multenterbox(msg, title, fieldNames, size)

    while True:
        error_msg = ''
        if fieldValues == None:
            break
        try:
            width = int(fieldValues[0].strip())
        except:
            error_msg += 'the width must be int'
        try:
            height = int(fieldValues[1].strip())
        except:
            error_msg += 'the height must be int' 
        if error_msg == '':
            break

        fieldValues = g.multenterbox(error_msg, title, fieldNames, fieldValues)

    url = 'http://placekitten.com/g/%d/%d' % (width, height)

    response = u_req.urlopen(url)
    cat_image = response.read()

    filepath = g.diropenbox('please choose the folder that store the cat image')

    if filepath:
        filename = '%s/cat_%d_%d.jpg' % (filepath, width, height)
    else:
        filename = 'cat_%d_%d.jpg' % (width, height)

    with open(filename, 'wb') as f:
        f.write(cat_image)      

if __name__ == "__main__":
    main()
