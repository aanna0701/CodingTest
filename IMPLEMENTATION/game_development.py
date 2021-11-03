n, m = map(int, input().split())

x, y, direction = map(int, input().split())

map_ = list()
for _ in range(n):
    map_.append(list(map(int, input().split())))
    
check = [[0]*m for _ in range(n)]
check[x][y] = 1

dx = (-1, 0, +1, 0)
dy = (0, +1, 0, -1)

def turn_left():
    global direction
    
    if direction == 0:
        direction = 3
    
    else:
        direction -= 1
    

cnt = 1
turn = 0

while(True):
    turn_left() # 왼쪽으로 방향 전환
    move_x = x + dx[direction]
    move_y = y + dy[direction]
    
    # 육지이고, 가본적 없으면 왼쪽으로 이동
    if map_[move_x][move_y] == 0 and check[move_x][move_y] == 0:
        x, y = move_x, move_y
        check[x][y] = 1
        cnt += 1
        turn = 0
        
        continue
    
    else:
        turn += 1
        
    if turn == 4:
        back_x = x - dx[direction]
        back_y = y - dy[direction]
        
        if map_[back_x][back_y] == 1:
            break
        
        else:
            x, y = back_x, back_y            
        turn = 0


print(cnt)      