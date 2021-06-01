def female_switch(arr, idx):
    start_idx = idx
    end_idx = idx
    while start_idx - 1 >= 0 and end_idx + 1 < len(arr):    
        if arr[start_idx-1] == arr[end_idx+1]:
            start_idx -= 1
            end_idx += 1
        else:
            break
    
    for i in range(start_idx, end_idx+1):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

switch_num = int(input())
switch_arr = list(map(int, input().split()))

student_num = int(input())

for i in range(student_num):
    gender, own_switch = map(int, input().split())
    
    if gender == 1:
        for i in range(own_switch-1,switch_num,own_switch):
            if switch_arr[i]:
                switch_arr[i] = 0
            else:
                switch_arr[i] = 1
    else:
        switch_arr = female_switch(switch_arr, own_switch-1)

print(*switch_arr)