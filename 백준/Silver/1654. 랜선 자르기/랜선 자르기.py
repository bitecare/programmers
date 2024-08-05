a, b = map(int, input().split())

lists = []
for _ in range(a):
   lists.append(int(input()))

sums = sum(lists)

def is_possible(length):
    return sum(x//length for x in lists)>=b

left, right = 1, max(lists)
length = 0

while right >= left :
    mid = int((left+right)/2)
    
    if is_possible(mid) :
        length = mid
        left = mid + 1
    else :
        right = mid - 1

print(length)
    