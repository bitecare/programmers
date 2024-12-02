n, m = map(int, input().split())

lists = []

def backtracking():
    global m 
    if m == len(lists):
        print(*lists)
        return
    for i in range(1, n+1):
        lists.append(i)
        backtracking()
        lists.pop()
            
backtracking()        