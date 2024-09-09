num = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [i*j for i,j in zip(sorted(a, reverse=True),sorted(b))]
print(sum(ans))