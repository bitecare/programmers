import sys

cnt = 0

while True:
    num = int(sys.stdin.readline())
    stu_lists = []
    let_lists = []
    
    if num == 0:
        break
        
    else :
        n_cnt = 0
        cnt +=1
        
        for _ in range(num):
            lists = sys.stdin.readline().split()
            stu_lists.append(lists[0])
            let_lists.append(lists[1:])

        print(f"Group {cnt}")
            
        for i in range(len(stu_lists)):
            if "N" in let_lists[i] :
                for j in range(len(let_lists[i])):
                    if let_lists[i][j] == "N":
                        print(f"{stu_lists[::-1][j]} was nasty about {stu_lists[0]}")
            else :
                n_cnt +=1
                pass
            stu_lists = stu_lists[1:] + [stu_lists[0]]

        if n_cnt == num :
            print("Nobody was nasty")
        print("")