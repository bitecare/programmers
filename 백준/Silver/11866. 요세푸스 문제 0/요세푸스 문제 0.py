from collections import deque

a, b = map(int, input().split())

lists = deque([i for i in range(1, a+1)])
answer = []
cnt = 0
while lists:
    cnt +=1
    if cnt % b !=0:
        c=lists.popleft()
        lists.append(c)
    else :
        c = lists.popleft()
        answer.append(str(c))

print('<'+', '.join(answer)+'>')    