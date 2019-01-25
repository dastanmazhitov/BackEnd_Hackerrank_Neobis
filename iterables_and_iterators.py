from itertools import combinations

n=input()
string=input().split()
k=int(input())
combin=list(combinations(string,k))
count=[i for i in combin if 'a' in i]
print(len(count)/len(combin))

