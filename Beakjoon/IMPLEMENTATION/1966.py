from collections import deque

n_test = int(input())

def q_custom(d, importances):
    cnt = 0
    
    q = deque(importances)
    
    while(q):
        
        max_i = max(list(q))
        pop = q.popleft()
        d -= 1 
        
        if pop == max_i:
            cnt +=1
                        
            if d == -1:
                print(cnt)
                break           
                       
            continue
        
        else:
            q.append(pop)
            
            if d == -1:
                d = len(q)-1
            

for _ in range(n_test):
    n, d = map(int, input().split())
    importances = list(map(int, input().split()))
    q_custom(n, d, importances)