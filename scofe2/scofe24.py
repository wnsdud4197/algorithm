n = int(input())

arr = []

for _ in range(n):
    arr.append(input())

arr.sort(key=lambda x: len(x), reverse=True)

q = int(input())

for _ in range(q):
    cnt = 0
    temp = input()
    for i in arr:
        if len(i) < len(temp):
            break
        if temp in i:
            cnt += 1
    print(cnt)