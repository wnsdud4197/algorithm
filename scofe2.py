k = int(input())

for tc in range(k):
    n, m = map(int, input().split())

    cnt = 0

    if n < 5:
        print(cnt)
        continue
    
    if n >= 5 and m >= 7:
        temp = min(n // 5, m // 7)
        n -= temp*5
        m -= temp*7
        cnt += temp

    lenx = n // 5

    for i in range(lenx):
        for j in range(8):
            if n >= (5 + j) and m >= (7-j):
                n -= (5 + j)
                m -= (7 - j)
                cnt += 1
                break
        if m == 0:
            cnt += (n // 12)
            break
            
    print(cnt)
    


