n = int(input())

start_time = []

end_time = []

for i in range(n):
    x = list(input().split('~'))

    start_time.append((x[0].strip().split(':')))
    end_time.append((x[1].strip().split(':')))

start_time.sort(key= lambda x : (x[0], x[1]))

end_time.sort(key= lambda x : (x[0], x[1]))

if int(start_time[-1][0]) > int(end_time[0][0]):
    print(-1)
elif int(start_time[-1][0]) == int(end_time[0][0]) and int(start_time[-1][1]) > int(end_time[0][1]):
    print(-1)
else:
    print(f'{start_time[-1][0]}:{start_time[-1][1]} ~ {end_time[0][0]}:{end_time[0][1]}') 