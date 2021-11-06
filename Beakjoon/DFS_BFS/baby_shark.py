space_size = int(input())
size = list()
for _ in range(space_size):
    size.append(list(map(int, input().split())))

from collections import deque


x, y = (0, 0)
break_init = 0
for i in range(space_size):
    for j in range(space_size):
        if size[i][j] == 9:
            break_init = 1
            x, y = (i, j)
            break
    if break_init:
        break

dx = (-1, 0, 0, +1)
dy = (0, -1, +1, 0)

size[x][y] = 2
time = 0

def bfs(x, y):
    
    q = deque()
    q.append((x, y))
    visit = [[0]*space_size for _ in range(space_size)]
    visit[x][y] = 1
    
    distance = [[0]*space_size for _ in range(space_size)]
    eat = list()
    current_size = size[x][y]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]
            
            if m_x < 0 or m_x > space_size-1 or m_y < 0 or m_y > space_size-1:
                continue
            
            if size[m_x][m_y] > current_size or visit[m_x][m_y] == 1:
                continue    
            
            q.append((m_x, m_y))
            distance[m_x][m_y] = distance[x][y] + 1
            visit[m_x][m_y] = 1
            
            if size[m_x][m_y] > 0 and size[m_x][m_y] < current_size:
                eat.append((distance[m_x][m_y], m_x, m_y))
        
        # 0, 2, 1 우선 순위로 정렬
        eat.sort(key = lambda x:(x[0], x[1], x[2]))
                
    return eat
       
cnt = 0

while(True):    
    
    eat = bfs(x, y)
    
    if not eat:
        print(time)
        break
    
    eat = eat[0]
    time += eat[0]
    cnt += 1
    size[eat[1]][eat[2]] = size[x][y]
    size[x][y] = 0
    
    x, y = eat[1], eat[2]
    
    if cnt == size[eat[1]][eat[2]]:
        size[eat[1]][eat[2]] += 1
        cnt = 0