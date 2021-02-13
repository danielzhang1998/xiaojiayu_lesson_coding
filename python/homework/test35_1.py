from os import error
import easygui as g

msg = 'enter the information!'
title = 'count'
fieldNames = ['*Username','*Name','Telephone','*Phone','QQ','*E-mail']
fieldValues = g.multenterbox(msg, title, fieldNames)

while True:
    if fieldValues == None:
        break
    errormsg = ''
    for i in range(len(fieldNames)):
        if fieldValues[i] == '' and '*' in fieldNames[i]:
            errormsg += fieldNames[i] + 'it is necessary to enter\n'

    if errormsg == '':
        break
    fieldValues = g.multenterbox(errormsg, title, fieldNames, fieldValues)

print(str(fieldValues))