# n, m, k 입력
n, m, k = map(int, input().split())

# 입력을 배열로
array = list(map(int, input().split()))

array.sort(reverse=True)

num_1st = k*(m//(k+1))+(m%(k+1))
num_2nd = m - num_1st

result = num_1st * array[0] + num_2nd * array[1]

print(result)