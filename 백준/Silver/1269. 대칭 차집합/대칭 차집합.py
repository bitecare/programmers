a, b = map(int, input().split())

group_a = set(map(int, input().split()))

group_b = set(map(int, input().split()))

a_b = (group_a - group_b)

b_a = (group_b - group_a)

print(len(a_b) + len(b_a))