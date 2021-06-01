T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    test = [0]*8
    while N > 0:
        if N >= 50000:
            test[0] = N // 50000
            N = N%50000
        elif N >= 10000:
            test[1] = N // 10000
            N = N%10000
        elif N >= 5000:
            test[2] = N // 5000
            N = N%5000
        elif N >= 1000:
            test[3] = N // 1000
            N = N%1000
        elif N >= 500:
            test[4] = N // 500
            N = N%500
        elif N >= 100:
            test[5] = N // 100
            N = N%100      
        elif N >= 50:
            test[6] = N // 50
            N = N%50
        elif N >= 10:
            test[7] = N // 10
            N = N%10
        else:
            break

    print('#{}'.format(test_case))
    for t in test:
        print(t, end=' ')
    print()
        