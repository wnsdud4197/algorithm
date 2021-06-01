N = int(input())
idx = 1
result = []

while idx <= N:
    cnt = 0
    num_list = list(str(idx))
    cnt += num_list.count('3')
    cnt += num_list.count('6')
    cnt += num_list.count('9')
    if cnt == 0:
        result.append(str(idx)) 
    else:
        result.append('-'*cnt)
    idx += 1

print(' '.join(result))
