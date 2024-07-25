import copy

a, b = map(int, input().split())
c = copy.deepcopy(a)
d = copy.deepcopy(b)

if b >= a:
    a, b = b , a

while b > 0:
    a, b = b, a % b

print((c // a) * (d // a) * a)