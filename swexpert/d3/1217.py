def func(x, y):
    if y==1:
        return x
    y-=1
    return x*func(x, y)

for test in range(1,11):
    testcase = int(input())
    N, M = map(int, input().split())
    result = func(N, M)
    print(f'#{testcase} {result}')