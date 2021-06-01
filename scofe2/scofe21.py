n, prac_time = input().split()

n = int(n)

temp_lst = list(map(int, prac_time.split(':')))

prac_time = temp_lst[0] * 3600 + temp_lst[1] * 60 + temp_lst[2]

play_list = []

for _ in range(n):
    temp_lst = list(map(int, input().split(':')))
    play_list.append(temp_lst[0] * 60 + temp_lst[1])

temp_lst = [0] * n

for i in range(n):
    temp = 0
    cnt = 0
    for j in range(i,n):
        cnt += 1
        temp += play_list[j]
        if temp >= prac_time:
            temp_lst[i] = cnt
            break

print(max(temp_lst), temp_lst.index(max(temp_lst)) + 1)
