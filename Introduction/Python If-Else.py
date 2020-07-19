def checkWeird(n):
    word = ""
    if n%2 != 0:
        word = "Weird"
    if n%2 == 0:
        if n>=2 and n<=5:
            word = "Not Weird"
        elif n>=6 and n<=20:
            word = "Weird"
        elif n>20:
            word = "Not Weird"
    return word

n = int(input())
print(checkWeird(n))