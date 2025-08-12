from collections import deque

n, k = map(int, input().split())

lists = [-1] * (100000 + 1)
lists[n] = 0
q = deque([n])

while q :
    queue = q.popleft()
    if queue == k:
        print(lists[queue])
        break
    else:
        for i in (queue -1, queue + 1, queue * 2):
            if 0 <= i <= 100000 and lists[i] == -1:
                lists[i] = lists[queue] + 1
                q.append(i)
                