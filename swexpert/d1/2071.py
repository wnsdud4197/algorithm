T = 1

test = list(map(int, input().split()))

sum_num = 0
cnt = len(test)
for i in test:
    sum_num += i
avg_num = int(sum_num / cnt)

print('#{} {}'.format(T, avg_num))