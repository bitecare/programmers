n = int(input())

for _ in range(n):
    num = int(input())
    lists = list(map(int, input().split()))
    team_count = len(set(lists))
    team_list = [[i+1, 0] for i in range(team_count)]

    for i in lists:
        team_list[i-1][1] +=1
        
    team_list = [i for i in team_list if i[1] == 6]
            
    check_list = [i[0] for i in team_list]
    team_list = [[i[0]] for i in team_list]
    
    cnt = 1
    for i in lists:
        if i in check_list:
            team_list[check_list.index(i)].append(cnt)
            cnt +=1
    sums = []
    for i in team_list:
        sums.append([i[0], sum(i[1:5]),i[5]])

    ans = sorted(sums, key = lambda x : (x[1], x[2]))

    print(ans[0][0])
