size = int(input())
directions = input().split()

coord = dict()
coord['x'] = 1
coord['y'] = 1

move = dict()
move['R'] = (+1, 0)
move['L'] = (-1, 0)
move['U'] = (0, -1)
move['D'] = (0, +1)

for direction in directions:
    m = move[direction]
    m_x = coord['x'] + m[0] 
    m_y = coord['y'] + m[1] 
    if m_x < 1 or m_x > size or m_y < 1 or m_y > size:
       continue
       
    else:   
        coord['x'] += m[0]
        coord['y'] += m[1]

print(f'{coord["y"]} {coord["x"]}')