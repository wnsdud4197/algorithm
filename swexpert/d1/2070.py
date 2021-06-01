T = int(input())

for test_case in range(1, T + 1):
    test = list(map(int, input().split()))
    
    prefer = ''

    if test[0] > test[1]:
        prefer = '>'
    elif test[0] < test[1]:
        prefer = '<'
    elif test[0] = test[1]:
        prefer = '='
    
    print('#{} {}'.format(T, sum_test))