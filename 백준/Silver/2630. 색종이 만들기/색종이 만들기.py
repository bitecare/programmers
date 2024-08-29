def divide(lists, blue, white):
    a = [row[:len(lists)//2] for row in lists[:len(lists)//2]]
    b = [row[:len(lists)//2] for row in lists[len(lists)//2:]]
    c = [row[len(lists)//2:] for row in lists[:len(lists)//2]]
    d = [row[len(lists)//2:] for row in lists[len(lists)//2:]]

    blue, white = check(a, blue, white)
    blue, white = check(b, blue, white)
    blue, white = check(c, blue, white)
    blue, white = check(d, blue, white)

    return blue, white


def check(lists,blue,white):
    sums = 0
    for i in range(len(lists)):
        sums += sum(lists[i])
    if sums == 0:
        white +=1
    elif sums == len((lists) * len(lists)):
        blue +=1
    else :
        blue, white = divide(lists, blue, white)
    return blue, white


num = int(input())

lists = []
blue = 0
white = 0

for _ in range(num):
    lists.append(list(map(int, input().split())))
blue, white = check(lists, blue, white)

print(white)
print(blue)