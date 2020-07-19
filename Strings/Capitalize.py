
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)
    s[0] = s[0].upper()
    
    for char in range(0,len(s)):
        if s[char] == ' ':
            s[char+1] = s[char+1].upper()
    s = ''.join(s)    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()