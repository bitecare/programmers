import sys

def eratosthenes(n):

    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

        p +=1

    prime_numbers = [p for p in range(2, n+1) if prime[p]]
    return prime_numbers

n = 1000000
lists = eratosthenes(n)
prime_set = set(lists)
            
num = int(input())

for _ in range(num):
    a = int(input())
    cnt = 0
    for i in lists:
        if i > a//2 :
            break
        if (a - i) in prime_set:
            cnt +=1

    print(cnt)