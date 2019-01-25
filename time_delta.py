from datetime import datetime

t = int(input())

for i in range(t):
    t1 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    t2 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    result = abs(int((t1 - t2).total_seconds()))
    print(result)
