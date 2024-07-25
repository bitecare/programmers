num = int(input())

def GCD(a, b) :
    if b >= a :
        a, b = b, a
    while b > 0 :
        a, b = b, a%b
    return a

def GCD_N(arr) :
    gcd = arr[0]
    for item in arr:
        gcd = GCD(gcd, item)
    return gcd

lists = []
for _ in range(num):
    lists.append(int(input()))

lists_b = []
for i in range(len(lists)-1) :
    lists_b.append(lists[i+1] - lists[i])

gcd = GCD_N(lists_b)

ans = (sum(lists_b) // gcd) - len(lists_b)
print(ans)