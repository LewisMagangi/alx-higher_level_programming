#!/usr/bin/python3
def uppercase(str):
        for l in range(len(str)):
                print("{}".format(str[l] if ord(str[l]) < 97 or ord(str[l]) >
                                  123 else chr(ord(str[l]) - 32)), end="")
        print()
