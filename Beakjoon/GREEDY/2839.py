n = int(input())
n_5 = 0
n_3 = 0
result = 0
tmp = 0


while(n >= 0):
    
    r_5 = n % 5
    r_3 = n % 3
    
    n_5 = n // 5
    n_3 = n // 3
    
    if r_5 == 0:
        result += n_5
        print(result)
        break
    
    n-= 3
    result += 1
    
else:
    print(-1)