T = int(input())

for test_case in range(1, T + 1):
    s, p, q, m = map(int, input().split())
    temp = s
    cnt_lst = [0]*m
    idx = 0
    while True:
        generate = (temp * p + q) % m
        if cnt_lst[generate]:
            result = idx - cnt_lst[generate]
            break
        else:
            cnt_lst[generate] += idx
            temp = generate
            idx += 1

    print('#{} {}'.format(test_case, result))