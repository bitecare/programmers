words = input()
num = int(input())

for _ in range(num):
    lists = input().split()
    n1 = int(lists[1])
    n2 = int(lists[2])
    print(words[n1:n2+1].count(lists[0]))