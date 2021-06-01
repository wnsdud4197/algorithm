N = int(input())
lst = list(map(int, input().split()))

lst.sort()

reulst = 0
cnt = 0

for i in lst:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)