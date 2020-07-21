# Enter your code here. Read input from STDIN. Print output to STDOUT


def takeInput():
    try:
        a, b = list(map(int, input().split()))
        print(a // b)
    except ZeroDivisionError as error:
        print('Error Code:', error)
    except ValueError as error:
        print('Error Code:', error)


n = int(input())
for _ in range(n):
    takeInput()