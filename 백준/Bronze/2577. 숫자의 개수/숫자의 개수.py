a = int(input())
b = int(input())
c = int(input())

result = a * b * c
dic = {"0" : 0, "1" : 0, "2" : 0, "3" : 0,
      "4" : 0, "5" : 0, "6" : 0, "7" : 0,
      "8" : 0, "9" : 0}
for i in str(result):
    if i in dic:
        dic[i] += 1


for i in dic.values():
    print(i)