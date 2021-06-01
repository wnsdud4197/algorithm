import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(input()))

start_idx = []

for i in range(n):
    if arr[0][i] == 'c':
        start_idx.append(i)

dx = [1, 0, 0]
dy = [0, -1, 1]

def bfs(start_idx):

    temp = [[0 for _ in range(n)] for _ in range(m)]
    my_queue = []
    my_queue.append((0, start_idx))

    while my_queue:
        x, y = my_queue.pop(0)

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if arr[nx][ny] == 'x':
                continue

            if temp[nx][ny] != 0:
                continue
            
            if arr[nx][ny] == '.' and (i == 1 or i == 2):
                temp[nx][ny] = temp[x][y] + 1
                my_queue.append((nx,ny))

            elif arr[nx][ny] == '.':
                temp[nx][ny] = temp[x][y]
                if nx == (m - 1):
                    return temp[nx][ny]
                my_queue.append((nx,ny))

    return -1

min_change = 987654321

for i in start_idx:
    result = bfs(i)
    
    if result != -1:
        min_change = min(result, min_change)

if min_change == 987654321:
    print(-1)
else:
    print(min_change)