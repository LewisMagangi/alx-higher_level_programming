#!/usr/bin/env python3
def no_c(my_string):
    x = list(my_string)
    count = 0
    for i in x:
        if i == "c" or i == "C":
            x[count] = ""
        count += 1

    return "".join(x)
