num = int(input())

lists = [1,1,2,2,2,2,2,2,2,1]

if num == 1:
    print(9%1000000000)

elif num == 2:
    print(sum(lists))
else :
    for i in range(2,num):
        answer = [0]*10
        answer[0] = lists[1]
        answer[1] = lists[0] + lists[2]
        answer[2] = lists[1] + lists[3]
        answer[3] = lists[2] + lists[4]
        answer[4] = lists[3] + lists[5]
        answer[5] = lists[4] + lists[6]
        answer[6] = lists[5] + lists[7]
        answer[7] = lists[6] + lists[8]
        answer[8] = lists[7] + lists[9]
        answer[9] = lists[8]

        lists = answer
        
    print(sum(answer)%1000000000)      