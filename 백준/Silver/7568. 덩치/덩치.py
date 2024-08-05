num = int(input())

height = []
weight = []
for _ in range(num):
    a, b = map(int, input().split())
    height.append(a)
    weight.append(b)

ans = []
for i in range(len(height)):
    cnt = 0
    for j in range(len(height)):
        if height[i] < height[j] and weight[i] < weight[j] :
            cnt +=1
    ans.append(cnt+1)
print(*ans)