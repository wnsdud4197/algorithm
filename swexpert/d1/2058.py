T = int(input())
 
sum_num = 0
 
while True:
    sum_num += T % 10
    T = T // 10
    if T == 0 : break
 
print(sum_num)