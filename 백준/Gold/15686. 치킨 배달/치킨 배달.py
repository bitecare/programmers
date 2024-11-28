num, chicken = map(int, input().split())
city_map = []
for _ in range(num):
    city_map.append(list(map(int, input().split())))

house_list = []
chicken_list = []
visited = [False] * len(chicken_list)  # 치킨집 개수만큼 초기화
min_diff = float('inf')  # 최소값 초기화

# 집과 치킨집 위치 저장
for i in range(num):
    for j in range(num):
        if city_map[i][j] == 1:
            house_list.append([i, j])
        elif city_map[i][j] == 2:
            chicken_list.append([i, j])

# 거리 계산 함수
def calculate(house_list, selected_chicken_list):
    total_distance = 0
    for house in house_list:
        min_distance = float('inf')
        for chicken in selected_chicken_list:
            distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

# 백트래킹 함수
def backtrack(depth, idx, selected_chicken):
    global min_diff
    if depth == chicken:
        # 선택된 치킨집으로 거리 계산
        diff = calculate(house_list, selected_chicken)
        min_diff = min(min_diff, diff)
        return

    for i in range(idx, len(chicken_list)):
        selected_chicken.append(chicken_list[i])
        backtrack(depth + 1, i + 1, selected_chicken)
        selected_chicken.pop()

# 시작
backtrack(0, 0, [])
print(min_diff)
