import sys
sys.stdin = open('input_1974.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    test = [0] * 9
    for i in range(9):
        test[i] = list(map(int, input().split()))
    
    n = 0
    result = 1
    print(test)
    while n < 9:
        for x in range(9):
            tempX = [0] * 9
            tempY = [0] * 9
            tempZ = [0] * 9
        # x축 검증
            for i in range(9):
                tempX[test[x][i]-1] += 1
            
            for t in tempX:
                if t != 1:
                    result = 0
        # y축 검증
            for j in range(9):
                tempY[test[j][x]-1] += 1

            for t in tempY:
                if t != 1:
                    result =0
        # 9칸 검증
            for k in range(9):
                tempZ[test[(n//3)*3+k//3][(n%3)*3+k%3]-1] += 1
            
            for t in tempZ:
                if t != 1:
                    result = 0

        if result == 0:
            break

        n += 1

    print('#{} {}'.format(test_case, result))