def permute(arr, cnt):
    result = [arr[:]]
    if :
        pass
    else:

        return result


T = int(input())

for TC in range(1, T + 1):
    arr, N = map(int, input().split())
    lst = []
    while arr > 0:
        lst.insert(0, arr%10)
        arr //= 10
    print(permute(lst))

