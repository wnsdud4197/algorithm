arr = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            if arr[i][j] != 1:
                arr[i][j] += 1
                result += 1
print(result)