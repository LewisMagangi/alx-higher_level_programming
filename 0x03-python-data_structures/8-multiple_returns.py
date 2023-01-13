#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x:
        y = sentence[0]
    else:
        y = None
    list_sent = [x, y]
    return tuple(list_sent)
