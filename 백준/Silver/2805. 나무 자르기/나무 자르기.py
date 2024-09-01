a, b = map(int, input().split())

lists = list(map(int, input().split()))

mins = 0
maxs = max(lists)
result = 0

while (mins <= maxs):
    middle = (maxs + mins)//2
    cutted_list = [0 if i < middle else i-middle for i in lists]
    total_cuts = sum(cutted_list)  

    if total_cuts >= b:
        result = middle
        mins = middle + 1
    else :
        maxs = middle - 1

print(result)