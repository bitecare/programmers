a = int(input())

answer = 0

if a < 100:
    for i in range(100+1):
        if a == i + sum([int(j) for j in str(i)]):
            answer = i
            break
    print(answer)
            

else :
    b = a - int(9 * len(str(a)))
    
    for i in range(a-b, a+1):
        if a == i + sum([int(j) for j in str(i)]) :
            answer = i
            break

    print(answer)
