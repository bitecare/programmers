import numpy as np

def solution(n, results):
    
    answer = 0
    match = np.full((n, n), None)
    
    for i in range(len(match)) :
        match[i][i] = 0
    
    for j in results:
        match[j[0]-1][j[1]-1] = 1
        match[j[1]-1][j[0]-1] = -1
        
    for a in range(n) :
        for b in range(n) :
            for c in range(n) :
                if match[b][a] == 1 and match[a][c] == 1:
                    match[b][c] = 1
                if match[b][a] == -1 and match[a][c] == -1:
                    match[b][c] = -1
                
    for k in match :
        if None not in k :
            answer +=1       
    return answer