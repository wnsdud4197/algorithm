T = int(input())

for test_case in range(1, T + 1):
    test = input()
    
    result = 1
    
    for i in range(len(test)//2):
        if test[i] != test[len(test)-1-i]:
            result = 0



    print('#{} {}'.format(test_case, result))