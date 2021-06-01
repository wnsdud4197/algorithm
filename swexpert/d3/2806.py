T = int(input())

for TC in range(1, T + 1):
    n = int(input())

    def nQueen(idx):
        if idx == n:
            check_queen()
        else:
            idx += 1
            arr[] = 1
            nQueen(idx)
            idx -= 1
            arr[] = 0
            