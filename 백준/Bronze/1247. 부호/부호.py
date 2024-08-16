for _ in range(3):

    num = int(input())
    sums = 0

    for _ in range(num):
        sums += int(input())
    if sums == 0 :
        print(0)
    elif sums > 0 :
        print("+")
    else :
        print("-")