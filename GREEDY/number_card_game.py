# 행과 열 입력 받기
n, m = map(int, input().split())

result = 0
for _ in range(n):
    tmp_list = list(map(int, input().split()))
    tmp_list.sort()
    min_value = tmp_list[0]
    if result < min_value:
        result = min_value

print(result)