# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
mbcAngle = int(round(math.degrees(math.atan(ab/bc)),0))
print(str(mbcAngle)+'°')
