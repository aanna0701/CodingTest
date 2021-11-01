change = 1260

count = 0

units = [500, 100, 50, 10]

for unit in units:
    if change >= 10:
        num = change // unit
        count += num
        change -= unit * num
        
    else:
        break

print(count)