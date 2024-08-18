num = int(input())

lists = [1,3]
lists += [0] * (num-1)

if num <= 2:
    print(lists[num-1]%10007)
else :
    for i in range(2, num+1):
        lists[i] = lists[i-2] * 2 + lists[i-1]
    print(lists[num-1]%10007)