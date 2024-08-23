num = int(input())

lists = []
for i in range(2, num):
    if num % i == 0:
        lists.append(i)
sums = sum(lists) + 1 + num

if num == 1:
    print(1*5-24)
else :
    print(sums * 5 - 24)