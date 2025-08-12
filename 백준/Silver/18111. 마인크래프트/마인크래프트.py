import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())

lists = []
for _ in range(n):
    lists.append(list(map(int, input().split())))

min_height = 0
max_height = 256
best_time = 99999999
best_height = 0

for i in range(max_height+1): #0층부터 256층까지
    inventory = b
    req_block_sum = 0
    time_sums = 0
    
    for j in range(len(lists)):
        for k in range(len(lists[j])):
            req_block = i - lists[j][k] #목표로 하는 칸 - 원래 칸

            if req_block > 0 : # 블럭을 더 심어야 하는 경우
                time_sums += abs(req_block) * 1
                inventory -= abs(req_block)
            else : # 블럭을 제거해야 하는 경우
                time_sums += abs(req_block) * 2
                inventory += abs(req_block)
                
    if req_block_sum > inventory: #심어야 하는 블럭이 내가 가지고 있는 블럭보다 많으면
        pass
    else :
        if  time_sums < best_time or (time_sums == best_time and i > best_height):
            best_time = time_sums
            best_height = i

print(best_time, best_height)