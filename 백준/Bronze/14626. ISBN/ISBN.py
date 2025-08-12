words = input()
cnt = 0
sums = 0
weights = 1
check_weights = 0

for i in words:
    cnt +=1
    if cnt % 2 == 1:
        weights = 1
    else :
        weights = 3
    if i != '*':
        sums += weights * int(i)
    else :
        check_weights = weights

for i in range(10):
    if (sums + check_weights * i) % 10  == 0:
        break
        
print(i)