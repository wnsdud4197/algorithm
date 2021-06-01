T = int(input())

for test_case in range(1, T + 1):
    test_case_len = int(input())
    test = list(map(int, input().split()))

    sum_revenue = 0
    max_price = 0
    for day in test[::-1]:
        if max_price < day: max_price = day
        elif max_price > day: sum_revenue += max_price - day
        
        
    print('#{} {}'.format(test_case, sum_revenue))

