def fibo(n):

    zero_list = [1,0]
    one_list = [0,1]

    for i in range(2, n+1):
        zero_list.append(zero_list[i-2] + zero_list[i-1])
        one_list.append(one_list[i-2] + one_list[i-1])
    if n == 0:
        return 1,0
    elif n == 1:
        return 0,1
    else :
        return (zero_list[-1], one_list[-1]) 

num = int(input())

for _ in range(num):
    a = int(input())
    b = fibo(a)
    print(*b)