num = int(input())

name = {}
cnt = 0
for _ in range(num):
    
    a = input()
    
    if a == "ENTER" :
        name = {}
    
    else :
        if a not in name:
            cnt +=1
            name[a] = 1
print(cnt)
            