def cal_num(s, e, n, k):
    calnumber = 0

    if s == 0:
        pass
    elif s%(k-1):
        calnumber += (s//(k-1) + 1)
    else:
        calnumber += s//(k-1)

    if e == (n-1):
        pass
    elif (n-e-1)%(k-1):
        calnumber += ((n-e-1)//(k-1) + 1)
    else:
        calnumber += (n-e-1)//(k-1)
        
    return calnumber
    
n, k = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] == 1:
        idx = i
        break

min_num = n

for j in range(k):
    s = idx - (k-1) + j
    e = s+(k-1)
    if s < 0 or e >= n:
        continue
    else:
        min_num = min(cal_num(s, e, n, k), min_num)

print(min_num+1)



