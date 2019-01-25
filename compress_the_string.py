from itertools import groupby


S=str(input()) #Input string
Group=[list(j) for k,j in groupby(S)] #Группировка с groupby

for i in Group: #Цикл
    print((len(i),int(i[0])),end=' ')  #len() выводит количество, int(i[]) строку
