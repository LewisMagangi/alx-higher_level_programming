#!/usr/bin/python3
'''
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
'''
def text_indentation(text):
    '''
    a function that prints a text with 2 new lines after each of these characters: ., ? and :
    '''

    if type(text) != str:
        raise TypeError('text must be a string')
    l = list(text)
    x = 0
    while x < len(l):
        if l[x] in ['.', '?', ':']:
            l.remove(l[x + 1])
        x += 1
    print(''.join(l))
    '''for i in range(len(text)):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')'''
