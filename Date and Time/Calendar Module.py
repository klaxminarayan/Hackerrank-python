# Enter your code here. Read input from STDIN. Print output to STDOUT

import datetime

mm, dd, yyyy = map(int, input().split())
dd = datetime.datetime(year=yyyy, month=mm, day=dd)
print(dd.strftime('%A').upper())