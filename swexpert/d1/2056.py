T = int(input())

for test_case in range(1, T + 1):
    test = input()
    year = test[0:4]
    month = test[4:6]
    day = test[6:]
    mon_dict = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    if int(day) > 31 or int(day) == 0 or int(month) > 12 or int(month) == 0 or int(day) > mon_dict[month]:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}/{}/{}'.format(test_case, year, month, day))