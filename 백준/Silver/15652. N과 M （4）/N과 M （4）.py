n, m = map(int, input().split())

lists = []

def backtracking():
    global m
    if m == len(lists):
        print(*lists)
        return
    for i in range(1, n+1):
        if (len(lists) == 0) or (lists[-1] <= i):
            lists.append(i)
            backtracking()
            lists.pop()
            
backtracking()