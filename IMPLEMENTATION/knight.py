inputs = input()

row = int(inputs[1])
col = ord(inputs[0]) - ord('a') + 1

directions = [(-2, +1), (-2, -1), (+2, +1), (+2, -1), (-1, +2), (-1, -2), (+1, +2), (+1, -2)]

cnt = 0

for direction in directions:
    m_row = row + direction[0]
    m_col = col + direction[1]
    
    if m_row > 8 or m_row < 1 or m_col > 8 or m_col < 1:
        continue
    
    else:
        cnt += 1
        
print(cnt)