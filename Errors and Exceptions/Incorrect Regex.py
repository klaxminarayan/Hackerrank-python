# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def isValidRegex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


queries = int(input())
for _ in range(queries):
    regex = input()
    print(isValidRegex(regex))