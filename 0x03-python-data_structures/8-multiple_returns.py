#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    list_sent = [x, y]
    return tuple(list_sent)
