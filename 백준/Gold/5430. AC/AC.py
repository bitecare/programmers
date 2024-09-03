from collections import deque

def command(commands, input_lists):
    reversed = False
    
    for command in commands:
        if command == "R":
            reversed = not reversed 
        elif command == "D":
            if len(input_lists) == 0:
                return "error"
            if reversed:
                input_lists.pop()
            else:
                input_lists.popleft() 
    
    if reversed:
        input_lists.reverse() 
    
    return "[" + ",".join(map(str, input_lists)) + "]"

num = int(input())

for _ in range(num):
    commands = input()
    number = int(input())
    input_lists = input()

    input_lists = input_lists.replace("[", "").replace("]", "").strip()

    if input_lists == "":
        input_lists = deque()
    else:
        input_lists = deque([int(i) for i in input_lists.split(",")])

    result = command(commands, input_lists)

    print(result)