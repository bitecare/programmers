num = int(input())

for _ in range(num) :
    a, b = map(int, input().split())
    
    c, d = 1, 1
    for i in range(b, b-a, -1):
        c *= i
    for j in range(2, a+1):
        d *= j
    print(c//d)