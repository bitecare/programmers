num = int(input())
count2 = 0

def fib1(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def fib2(n):
    global count2
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        count2 +=1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

count1 = fib1(num-2) + fib1(num-1)
fib2(num)
print(count1, count2)