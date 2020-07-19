n = int(input())
intList = map(int, input().split())
intList = tuple(intList)
print(hash(intList))
