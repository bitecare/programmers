import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:
        print(*ans)
        return 
        
    for i in range(1, N+1):
        if i not in ans: 
            if len(ans) == 0 or (len(ans) >= 1 and ans[-1] < i):
                ans.append(i)
                back()
                ans.pop()

back()