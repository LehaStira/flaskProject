import re


def delete_reapiting(s):
    new_string = ''
    for ind, i in enumerate(s):
        if i == '-' and s[ind-1] == '-':
            continue
        else:
            new_string+=i
    return new_string


def delete_last_symbol(s):
    if s[-1] == '-':
        return s[:-1]
    else:
        return s
