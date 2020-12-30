# Enter your code here. Read input from STDIN. Print output to STDOUT
arr,count=[],{}
for _ in range(int(input())):
    arr.append(input())
for i in arr:
    count[i] = count.get(i,0)+1
print(len(list(count.values())))    
print(*(list(count.values())))
