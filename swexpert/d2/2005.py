T = int(input())

for test_case in range(1, T + 1):
    result = [1]
    N = int(input())
    print('#{}'.format(test_case))
    for x in range(N):
        print(' '.join(map(str, result)))
        result1 = result[:]
        result1.append(0)
        result2 = result[:]
        result2.insert(0,0)
        result = list(map(sum, zip(result1,result2)))