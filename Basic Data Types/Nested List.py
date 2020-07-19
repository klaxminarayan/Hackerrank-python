def getGrade(element):
    return element[1]


def getSecondMinGrade(array, minGrade):
    for i in range(len(array)):
        if array[i][1] != minGrade:
            return array[i][1]


def getNamesWithSecondMinGrade(array, secondMinGrade):
    names = []
    for i in range(len(array)):
        if array[i][1] == secondMinGrade:
            names.append(array[i][0])
    return names


students = int(input())
data = []

for i in range(students):
    name = input()
    grade = float(input())
    data.append([name, grade])

data.sort(key=getGrade)
minGrade = data[0][1]
#print(minGrade)

secondMinGrade = getSecondMinGrade(data, minGrade)
#print(secondMinGrade)

namesWithSecondMinGrade =  sorted(getNamesWithSecondMinGrade(data, secondMinGrade))

for name in namesWithSecondMinGrade:
    print(name)