import sys

num = int(sys.stdin.readline())

lists = []
for _ in range(num):
    
    command = list(map(int, sys.stdin.readline().split()))
    
    if command[0] == 1:
        lists.append(command[1])
        
    elif command[0] == 2:
        if lists:
            emp = lists.pop(-1)
            print(emp)
        else:
            print(-1)
            
    elif command[0] == 3:
        print(len(lists))
        
    elif command[0] == 4:
        if lists == [] :
            print(1)
        else :
            print(0)
            
    elif command[0] == 5:
        if lists != []:
            print(lists[-1])
        else :
            print(-1)
     
        