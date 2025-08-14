import sys
input = sys.stdin.readline

num = int(input())
lengths = int(input())

words = input()
pattern = "IOI" + "OI" * (num-1)

cnt = 0

for i in range(lengths - len(pattern) + 1):
    if words[i] == "I":
        if words[i : i + len(pattern)] == pattern :
            cnt +=1
print(cnt)