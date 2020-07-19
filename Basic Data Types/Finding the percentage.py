def avg(marks):
    return "{0:.2f}".format(sum(marks) / 3)
if __name__ == '__main__':
    n = int(input())
    studentMarks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        studentMarks[name] = scores
queryName = input()
print(avg(studentMarks[queryName]))
