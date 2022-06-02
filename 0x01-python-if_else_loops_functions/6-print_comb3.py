#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x >= y or (x == 8 and y == 9):
            continue
                print("{:d}{:d}".format(x, y), end=', ')
                print('{:d}'.format(89))
