n,m=(int(i) for i in input().split())
l=map(int,input().strip().split(' '))
a=set(map(int,input().strip().split(' ')))
b=set(map(int,input().strip().split(' ')))
happy=0

for i in l:
    if i in a:
        happy+=1
    if i in b:
        happy+=-1
print(happy)
