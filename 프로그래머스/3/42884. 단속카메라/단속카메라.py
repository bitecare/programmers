def solution(routes):
    
    answer = 1
    routes = sorted(routes, key = lambda x : x[1])
    
    lists = [routes[0][1]]
    
    for i,j in routes :
        if i > lists[-1] :
            lists.append(j)
            answer +=1
           
    return answer
