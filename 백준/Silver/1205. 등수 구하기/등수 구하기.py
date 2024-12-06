num, myscore, limit = map(int, input().split())
lists = []
answer = -1


if num >= 1:
    lists = list(map(int, input().split()))

lists.append(myscore)

same_score = lists.count(myscore)
same_score_count = 0

ans = sorted(lists,reverse=True)[:limit]

for i in range(len(ans)):
    if ans[i] == myscore:
        same_score_count +=1
        if same_score_count == same_score:
            answer = ans.index(myscore)+1
print(answer)