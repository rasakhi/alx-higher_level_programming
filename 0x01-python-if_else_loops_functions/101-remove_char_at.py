#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0) and (n < len(str)):
        updated_str = str.replace(str[n], '')
        return (updated_str)
    else:
        return (str)
