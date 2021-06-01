T = int(input())

for test_case in range(1, T + 1):
    test = list(map(int, input().split()))
    max_num = 0
    for i in test:
        if max_num < i:
            max_num = i
        
    print('#{} {}'.format(test_case, max_num))