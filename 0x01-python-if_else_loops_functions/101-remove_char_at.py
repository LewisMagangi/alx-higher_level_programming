#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = ""
    if n >= 0 and n < len(str):
        for i in range(len(str)):
            if i + 1 == n:
                i += 1
            else:
                strcp += str[i]
            return(print(strcp))
    else:
        return(print(str))
