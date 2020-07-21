def average(arr):
    arr = set(arr)
    arrSum = sum(arr)
    arrAvg = arrSum/len(arr)
    return arrAvg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)