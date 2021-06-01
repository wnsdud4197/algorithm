n = int(input())

arr = []

for _ in range(n):
	arr.append(list(map(int, input())))
	
temp = [[0 for _ in range(n)] for _ in range(n)]
	
for i in range(n):
	temp[0][i] = arr[0][i]
	temp[i][0] = arr[i][0]
    
for i in range(1,n):
	for j in range(i,n):
		if arr[j][i]:
			temp[j][i] = min(temp[j-1][i], temp[j][i-1], temp[j-1][i-1]) + 1
		else:
			temp[j][i] = 0
			
		if arr[i][j]:
			temp[i][j] = min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1]) + 1
		else:
			temp[i][j] = 0

box_arr = [0] * (n+1)

for i in range(n):
    for j in range(n):
        for k in range(1, temp[i][j]+1):
            box_arr[k] += 1

print(f'total: {sum(box_arr)}')

for i in range(1, n+1):
    if box_arr[i] == 0:
        break
    print(f'size[{i}]: {box_arr[i]}')
