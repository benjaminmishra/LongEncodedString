import math
import os
import random
import re
import sys



#
# Complete the 'frequency' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING s as parameter.
# s = 12(2)26#24#
def frequency(s:str) ->int:
    result = [0] * 26

    i = 0

    while i < len(s):
        # Handle multi-digit numbers with #
        if i + 1 < len(s) and s[i:i+2].isdigit():
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                i += 3
            else:
                num = int(s[i])
                i += 1
        else:
            num = int(s[i])
            i += 1

        # Handle count in brackets if present
        count = 1
        if i < len(s) and s[i] == '(':
            bracket_end = s.find(')', i)
            count = int(s[i+1:bracket_end])
            i = bracket_end + 1

        # Update frequency (adjust index as a=1 maps to index 0)
        result[num-1] = count

    return result

if __name__ == '__main__':

    ENCODED_STRING = "12(2)26#24#"

    output = frequency(ENCODED_STRING)

    print(output)
