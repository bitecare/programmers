a = int(input())

em_list = {}
for _ in range(a):
    name, status = input().split()
    
    if name not in em_list:
        em_list[name] = "enter"
    else :
        if status == "leave" :
            em_list[name] = "leave"
        else :
            em_list[name] = "enter"

ans = sorted([i for i,v in em_list.items() if v == "enter"], reverse=True)
for i in ans:
    print(i)
    