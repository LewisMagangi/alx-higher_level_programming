#!/usr/bin/env python3
def no_c(my_string):
    x = list(my_string)
    for i in range(0, len(x) - 1):
        if x[i] == "c" or x[i] == "C":
            x[i] = ""

    return("".join(x))
