n, r, c = map(int, input().split())
answer = 0
#r 행
#c 열
#n 2^n 배열
n = 2 ** n

while n >= 1:
    if r < n // 2 and c < n // 2 :
        location = 0
    elif r < n // 2 and c >= n // 2 :
        c = c - n // 2
        location = 1
    elif r >= n // 2 and c < n // 2 :
        r = r - n // 2
        location = 2
    else :
        c = c - n // 2
        r = r - n // 2
        location = 3
    answer = answer + location * (n // 2) ** 2
    n = n // 2

print(answer)