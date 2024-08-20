a = input()

ans = 10
for i in range(len(a[:-1])):
    if a[i] == a[i+1]:
        ans +=5
    else :
        ans +=10
print(ans)
    