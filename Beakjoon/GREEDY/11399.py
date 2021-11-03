n = int(input())
time = list(map(int, input().split()))

cum_t = 0
t = 0

time.sort()

for i in time:
    cum_t += i
    t += cum_t
    
print(t)