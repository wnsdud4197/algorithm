avg_point = list(map(float, (input().split())))

n, m = map(int, input().split())

my_status = []

for i in range(n):
    my_status.append(list(input()))

my_status_genre = []

for i in range(n):
    my_status_genre.append(list(input()))

dic = {
    'A': avg_point[0],
    'B': avg_point[1],
    'C': avg_point[2],
    'D': avg_point[3],
    'E': avg_point[4],
}

y_arr = []

o_arr = []

for i in range(n):
    for j in range(m):
        if my_status[i][j] == 'Y':
            y_arr.append((my_status_genre[i][j], dic[my_status_genre[i][j]], i, j))
        elif my_status[i][j] == 'O':
            o_arr.append((my_status_genre[i][j], dic[my_status_genre[i][j]], i, j))

y_arr.sort(key=lambda x: (-x[1], x[2], x[3]))
o_arr.sort(key=lambda x: (-x[1], x[2], x[3]))

for i in y_arr:
    print(f'{i[0]} {i[1]} {i[2]} {i[3]}')
for i in o_arr:
    print(f'{i[0]} {i[1]} {i[2]} {i[3]}')