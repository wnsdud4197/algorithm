# 홀수만 더하기
T = 3

test = list(map(int, input().split()))
sum_test = 0
for i in test:
    if i % 2:
        sum_test += i

print('#{} {}'.format(T, sum_test))