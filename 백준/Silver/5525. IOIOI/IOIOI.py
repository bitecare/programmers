import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

cnt = 0
i = 0
repeat = 0

while i < m - 2:
    if s[i : i + 3] == "IOI":
        repeat +=1
        if repeat >= n:
            cnt +=1
        i+=2
        
    else:
        repeat = 0
        i+=1
        
print(cnt)