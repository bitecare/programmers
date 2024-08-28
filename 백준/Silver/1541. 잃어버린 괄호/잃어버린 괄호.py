word = input()

lists = word.split("-")
 
for i in range(len(lists)):
    if "+" in lists[i] :
        lists[i] = sum([int(j) for j in lists[i].split("+")])
result = int(lists[0])
for i in lists[1:]:
    result -= int(i)
print(result)