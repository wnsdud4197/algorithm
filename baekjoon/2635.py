n = int(input())

max_arr = []
max_val = 0

for i in range(n,0,-1):
    cnt = 2
    idx = 0
    arr = [n, i]
    temp1 = arr[idx] - arr[idx+1]
    
    while temp1 >= 0:
        arr.append(temp1)
        idx += 1
        temp1 = arr[idx] - arr[idx+1]
        cnt += 1
    
    if max_val < cnt:
        max_val = cnt
        max_arr = arr[:]
    

print(max_val)
print(*max_arr)