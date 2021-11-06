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
    
    # 2차원 방문 배열
    visit = [[0]*space_size for _ in range(space_size)]
    visit[x][y] = 1
    
    # 2차원 거리 배열
    distance = [[0]*space_size for _ in range(space_size)]
    
    eat = list()
    
    # 현재 아기상어 크기
    current_size = size[x][y]
    
    while q:
        x, y = q.popleft()
        
        # 네 방향 탐색
        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]
            
            # 지도를 넘어간 경우 못지남
            if m_x < 0 or m_x > space_size-1 or m_y < 0 or m_y > space_size-1:
                continue
            
            # 아기 상어보다 큰 물고기와 이미 탐색한 경우 못지남
            if size[m_x][m_y] > current_size or visit[m_x][m_y] == 1:
                continue    
            
            # 조건 만족하면 탐색
            q.append((m_x, m_y))
            distance[m_x][m_y] = distance[x][y] + 1 # 기준점으로 부터 거리를 거리 배열에 표시
            visit[m_x][m_y] = 1                     # 방문 기록
            
            # 아기 상어 보다 크기가 작을경우 먹음
            if size[m_x][m_y] > 0 and size[m_x][m_y] < current_size:
                # 아기 상어로 부터 거리와 위치를 배열로 표시
                eat.append((distance[m_x][m_y], m_x, m_y))
        
        # 0, 2, 1 우선 순위로 정렬
        eat.sort(key = lambda x:(x[0], x[1], x[2]))
                
    return eat
       
cnt = 0

while(True):    
    
    eat = bfs(x, y)
    
    # 종료 조건: 더 이상 물고기가 없을 경우
    if not eat:
        print(time)
        break
    
    eat = eat[0]
    # 물고기를 먹는데 걸린 시간
    time += eat[0]
    # 경험치 표시
    cnt += 1
    # 물고기 위치 업데이트
    size[eat[1]][eat[2]] = size[x][y]
    size[x][y] = 0
    x, y = eat[1], eat[2]
    
    # 경험치가 차면 아기 상어 크기 증가
    if cnt == size[eat[1]][eat[2]]:
        size[eat[1]][eat[2]] += 1
        cnt = 0