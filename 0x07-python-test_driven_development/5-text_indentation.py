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
    for i in text:
        if i in ['.', '?', ':']:
            print('\n')
        else:
            print(i, end='')
