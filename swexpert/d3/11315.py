import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    test = [0] * N
    result = 'NO'

    for n in range(N):
        temp = [x for x in input()]
        test[n] = temp
    
    cntX = 0
    cntY = 0
    cntZ1 = 0
    cntZ2 = 0
    cntZ3 = 0
    cntZ4 = 0
    
    # x 축 검사
    for i in range(N):
        for j in range(N):
            if test[i][j] == 'o':
                cntX += 1
                if cntX >= 5:
                    result = 'YES'
            else:
                cntX = 0
        cntX = 0
    
    # y 축 검사
    for j in range(N):
        for i in range(N):
            if test[i][j] == 'o':
                cntY += 1
                if cntY >= 5:
                    result = 'YES'
            else:
                cntY = 0    
        cntY = 0

    # 오른쪽 아래 대각선 검사
    for n in range(N-4):
        for j in range(N-n):
            if test[j+n][j] == 'o':
                cntZ1 += 1
                if cntZ1 >= 5:
                    result = 'YES'
            else:
                cntZ1 = 0
            
            if test[j][j+n] == 'o':
                cntZ2 += 1
                if cntZ2 >= 5:
                    result = 'YES'
            else:
                cntZ2 = 0

    # 오른쪽 위 대각선 검사
    for n in range(N-4):
        for j in range(N-n):
            if test[j][N-1-n-j] == 'o':
                cntZ3 += 1
                if cntZ3 >= 5:
                    result = 'YES'
            else:
                cntZ3 = 0
            
            if test[n+j][N-1-j] == 'o':
                cntZ4 += 1
                if cntZ4 >= 5:
                    result = 'YES'
            else:
                cntZ4 = 0

    print('#{} {}'.format(test_case, result))