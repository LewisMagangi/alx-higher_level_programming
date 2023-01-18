#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = max(sorted(a_dictionary.values()))
        return list(a_dictionary.keys())[list(a_dictionary.values()).index(b)]
    else:
        return None
