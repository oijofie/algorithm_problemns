import unittest

def is_unique(string):
    str_list = []
    for char in string:
        if char in str_list:
            return False
        str_list.append(char)
    return True

str1 = 'ABC'
str2 = "abcc"

print(is_unique(str1))
print(is_unique(str2))
