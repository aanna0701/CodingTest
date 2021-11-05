from collections import deque

n, m = map(int, input().split())
temp = list()
for _ in range(n):
    temp.append(list(map(int, input())))
    
dx = (+1, 0, -1, 0)
dy = (0, +1, 0, -1)

cnt = 0


def bfs(x, y):
    
    if temp[x][y] == 0:
        
        return False
    
    queue = deque([[x, y]])

    while(queue):
        q = queue.popleft()
        
        x_ = q[0]
        y_ = q[1]
        
        temp[x_][y_] = 1
    
        for i in range(4):
            mx = x_ + dx[i]
            my = y_ + dy[i]
            
            if mx >= 0 and mx < n and my >= 0 and my < m:
                if temp[mx][my] == 0:
                    queue.append([mx, my])
                            
            else:
                continue
            
    return True    

for i in range(n):
    for j in range(m):
        if bfs(i, j):
            cnt += 1

print(cnt) 