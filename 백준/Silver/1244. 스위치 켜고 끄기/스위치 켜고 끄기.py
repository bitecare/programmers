num = int(input())
lists = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, place = map(int, input().split())

    if gender == 1:
        change_lists = [i-1 for i in range(place, num+1, place)]
        for i in change_lists:
            if lists[i] == 1:
                lists[i] = 0
            else :
                lists[i] = 1
    else :
        start, end = place-1, place-1
        check = True
        while check:
            if start > 0 and end < len(lists) - 1 and lists[start - 1] == lists[end + 1]:
                start -= 1
                end += 1
            else:
                check = False

        for i in range(start, end+1):
            if lists[i] == 1:
                lists[i] = 0
            else :
                lists[i] = 1

for i in range(0, len(lists), 20):
    print(*lists[i:i+20])