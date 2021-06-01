import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    students = [0] * N

    for n in range(N):
        test = list(map(int, input().split()))
        sum = test[0]*0.35 + test[1]*0.45 + test[2]*0.2
        students[n] = [n, sum]

    for i in range(N - 1, 0, -1):
        for j in range(i):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1]= students[j + 1], students[j]

    for idx in range(N):
       if students[idx][0] == K - 1:
           if idx >= N/10 * 9:
               result = 'A+'
               break
           elif idx >= N/10 * 8:
               result = 'A0'
               break
           elif idx >= N/10 * 7:
               result = 'A-'
               break
           elif idx >= N/10 * 6:
               result = 'B+'
               break
           elif idx >= N/10 * 5:
               result ='B0'
               break
           elif idx >= N/10 * 4:
               result = 'B-'
               break
           elif idx >= N/10 * 3:
               result = 'C+'
               break
           elif idx >= N/10 * 2:
               result = 'C0'
               break
           elif idx >= N/10 * 1:
               result = 'C-'
               break
           elif idx >= N/10 * 0:
               result = 'D0'
               break
           
           
    print('#{} {}'.format(test_case, result))