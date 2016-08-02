# 344. Reverse String
# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

def reverseString(s):

    return s[::-1]



def reverse_string(str):
    char_list = list(str)
    start = 0
    end = len(char_list) - 1
    while end > start:
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 1
        end -= 1
    
    return "".join(char_list)


# Lazy solution
def reverse_string_pythonic(input_str):
    '''
    This function use Python's slice notation
    array[start:end:step] # start through not past end, by step
    :param input_str:
    :return:
    '''
    return input_str[::-1]


# Naive solution!
def reverse_string_naive(input_str):
    result = ""
    for i in xrange(len(input_str) - 1, -1, -1):
        result += input_str[i]
    return result


str = "renhe"

print reverseString(str)