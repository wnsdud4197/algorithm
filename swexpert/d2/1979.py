import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    test = [0]*(N+2)

    test[0] = [0] * (N+2)
    for i in range(N):
        test[i+1] = [0] + list(map(int, input().split())) + [0]
    test[N+1] =[0] * (N+2)
    
    cnt = 0

    for i in range(N+2):
        temp_x = 0
        temp_y = 0
        for j in range(N+2):
            if test[i][j] == 1:
                temp_x += 1
            else:
                if temp_x == K:
                    cnt += 1
                temp_x = 0

            if test[j][i] == 1:
                temp_y += 1
            else:
                if temp_y == K:
                    cnt += 1
                temp_y = 0

    print("#{} {}".format(test_case, cnt))