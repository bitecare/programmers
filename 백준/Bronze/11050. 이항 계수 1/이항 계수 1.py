a, b = map(int, input().split())

prod_a = 1
prod_b = 1
for i in range(a,a-b,-1):
    prod_a *=i
    
for j in range(b,0,-1):
    prod_b *=j
    
print(prod_a//prod_b)