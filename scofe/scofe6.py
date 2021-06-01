n, m = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(map(int, input().split())))

temp = [[0 for _ in range(n)] for _ in range(m)]

temp[0][0] = arr[0][0]

for i in range(1,n):
    temp[0][i] = temp[0][i-1] + arr[0][i]

for i in range(1,m):
    temp[i][0] = temp[i-1][0] + arr[i][0]

for i in range(1,m):
    for j in range(1,n):
        temp[i][j] = max(temp[i-1][j], temp[i][j-1]) + arr[i][j]


print(temp[m-1][n-1])