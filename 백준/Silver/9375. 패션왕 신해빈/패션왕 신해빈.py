num = int(input())

for _ in range(num):
    kinds = int(input())
    clothes = {}
    ans = 1

    for _ in range(kinds):
        wear, type = input().split()

        if type not in clothes :
            clothes[type] = 2
        else :
            clothes[type] += 1

    for i in clothes.values():
        ans *=i
        
    print(ans-1)