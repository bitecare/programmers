import sys

#num = int(sys.stdin.readline())
num = int(input())


#lists = list(map(int, sys.stdin.readline().split()))
lists = list(map(int, input().split()))

dic = {}

for i in lists:
    if i not in dic:
        dic[i] =1
    else :
        dic[i] +=1

#num2 = int(sys.stdin.readline())
num2 = int(input())

lists2 = list(map(int, input().split()))
#lists2 = list(map(int, sys.stdin.readline().split()))

for i in range(len(lists2)):
    if lists2[i] in dic:
        lists2[i] = dic[lists2[i]]
    else :
        lists2[i] = 0

print(*lists2)
    