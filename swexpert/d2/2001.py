T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly_box = []
    for colum in range(N):
        test = list(map(int, input().split()))
        fly_box.append(test)

    max_fly = 0
    # for i in range(N-M+1):
    #     sum_fly = 0
    #     for j in range(M):
    #         sum_fly += sum(fly_box[i+j][j:j+M])
    #     if max_fly < sum_fly:
    #         max_fly = sum_fly

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for k in range(M):
                sum_fly += sum(fly_box[i+k][j:j+M])
        
            if max_fly < sum_fly:
                max_fly = sum_fly

    

    print('#{} {}'.format(test_case, max_fly))
