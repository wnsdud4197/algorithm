T = int(input())

for TC in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def dfs(i, j, c, s):
        for i in range(4):
            dn = i + dx[i]
            dm = j + dy[i]

            if dn >= 0 and dn < n and dm >= 0 and dm < n:
                dfs(dn, dm, c, s)
            