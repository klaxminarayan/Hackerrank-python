# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
arr=[]
for i in range(int(input())):
    arr.append(input().split())

for i in range(len(arr)):
    if 'append' in arr[i]:
        d.append(arr[i][1])
    elif 'appendleft' in arr[i]:
        d.appendleft(arr[i][1])
    elif 'pop' in arr[i]:
        d.pop()
    elif 'popleft' in arr[i]:
        d.popleft()
print(*(list(d)))
