# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
word,n = input().split()
n = int(n)
word = sorted(word)
for j in itertools.combinations_with_replacement(word,n):
    print(''.join(j))

