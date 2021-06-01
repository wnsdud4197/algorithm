T = int(input())
 
for test_case in range(1, T + 1):
    test = list(map(int, input().split()))
 
    for i in range(len(test) - 1, 0, -1):
        for j in range(i):
            if test[j] > test[j + 1]:
                test[j], test[j + 1] = test[j + 1], test[j]
 
    sum = 0 
 
    for i in test[1:len(test)-1]:
        sum += i

    sum /= 8
    sum *= 10
    avg = 0

    if sum % 10 >= 5:
        avg = (sum+10)//10
    else :
        avg = sum // 10
    

    print('#{} {}'.format(test_case, int(avg)))
