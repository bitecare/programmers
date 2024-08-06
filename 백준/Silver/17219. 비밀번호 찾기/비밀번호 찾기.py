import sys
input = sys.stdin.readline

a, b = map(int, input().split())

dic = {}

for _ in range(a):
    site, pw = input().split()
    dic[site] = pw

for _ in range(b):
    inputs = input().rstrip()
    print(dic[inputs])