import sys

input = sys.stdin.readline
num = int(input())

counts = [0] * 10001
for _ in range(num) :
    number = int(input())
    counts[number] +=1

for i in range(10001) :
    if counts[i] >= 1:
        for j in range(counts[i]) :
            print(i)