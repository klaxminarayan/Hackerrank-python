def swap_case(s):
    result = ""
    for let in s:
        if let.isupper():
            result += let.lower()
        else:
            result += let.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)