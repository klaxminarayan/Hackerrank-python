# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
"""
Only 4/6 Test Cases passed
n = int(input())
marks = input().split()
subMark=[]
totalMarks = 0
for i in range(N):
    students = namedtuple('student', marks)
    subMark = list(map(str,input().split()))[:4]
    student = students(subMark[0], subMark[1], subMark[3], subMark[3])
    totalMarks += int(student.MARKS)
print('{:.2f}'.format(totalMarks/n))
"""
# For all testcases..
n = int(input())
marks = input()
totalMarks = 0
Student = namedtuple('Student', marks)
for _ in range(n):
    student = Student(*input().split())
    totalMarks += int(student.MARKS)
print('{:.2f}'.format(totalMarks/n))
