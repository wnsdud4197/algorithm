T = int(input())

for test_case in range(1, T + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split())

    ans_hour = (hour1 + hour2 + (minute1 + minute2)//60)%12 
    if ans_hour == 0:
        ans_hour = 12
    ans_minute = (minute1 + minute2)%60

    print('#{} {} {}'.format(test_case, ans_hour, ans_minute))