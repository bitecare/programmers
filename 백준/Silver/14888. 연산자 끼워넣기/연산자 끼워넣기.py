num = int(input())
lists = list(map(int, input().split()))
plus, minus, multi, divid = map(int, input().split())

maximum = -1e9
minimum = 1e9

def DFS(depth, n, plus, minus, multi, divid):
    global maximum, minimum

    if depth == num:
        maximum = max(n, maximum)
        minimum = min(n, minimum)

    if plus :
        DFS(depth + 1, n + lists[depth], plus - 1, minus, multi, divid)
    if minus :
        DFS(depth + 1, n - lists[depth], plus, minus - 1, multi, divid)
    if multi :
        DFS(depth + 1, n * lists[depth], plus, minus, multi - 1, divid)
    if divid :
        DFS(depth + 1, int(n / lists[depth]), plus, minus, multi, divid - 1)

DFS(1, lists[0], plus, minus, multi, divid)
print(maximum)
print(minimum)
        
    