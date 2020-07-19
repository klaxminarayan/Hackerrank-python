# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word,n = input().split()
word = sorted(word)
n = int(n)
for i in range(1, n + 1):
    for j in combinations(word, i):
        print(''.join(j))
