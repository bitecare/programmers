num = int(input())

lists = list(map(int, input().split()))

unique_list = sorted(set(lists))

index_map = {value : index for index, value in enumerate(unique_list)}

answer = [index_map[i] for i in lists]

print(*answer)