a,b = map(int, input().split())
lists = []

for i in range(a):
    lists.append(list(map(int, input().split())))

ans = sorted(lists, key = lambda x : (x[1],x[2],x[3]), reverse=True)

for i in range(len(ans)):
    
    if i == 0:
        ans[i].append(1)
    else :
        if ans[i][1] == ans[i-1][1] and ans[i][2] == ans[i-1][2] and ans[i][3] == ans[i-1][3]:
            ans[i].append(ans[i-1][4])
        else :
            ans[i].append(i+1)

for i in ans:
    if i[0] == b:
        print(i[4])