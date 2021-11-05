n, m = map(int, input().split())
temp = list()
for _ in range(n):
    temp.append(list(map(int, input())))
    
from collections import deque

dx = (+1, 0, -1, 0)
dy = (0, +1, 0, -1)

print(temp)

def bfs(x, y):
        
    queue = deque([[x, y]])

    while(queue):
        q = queue.popleft()
        
        x_ = q[0]
        y_ = q[1]
            
        for i in range(4):
            mx = x_ + dx[i]
            my = y_ + dy[i]
            
            
            if mx >= 0 and mx < n and my >= 0 and my < m:
                if temp[mx][my] == 1:
                    queue.append([mx, my])
                    temp[mx][my] = temp[x_][y_] + 1
                    if mx == n-1 and my == m-1:
                        break
                            
            else:
                continue
            
        

bfs(0, 0)