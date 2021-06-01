import sys
sys.stdin = open('sample_input.txt', 'r')

dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

hexa = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

 
# 16진수를 2진수로 변환
def to_bin(lst):
    arr = []
    for i in lst:
        arr += hexa[i]
    return arr
 
# 정상적인 암호인지 구분
def decryption(arr):
    sum_arr = 0
    for i in range(7):
        if i % 2:
            sum_arr += arr[i]
        else:
            sum_arr += arr[i]*3
    sum_arr += arr[7]
 
    if sum_arr % 10:
        return 0
    else:
        return sum(arr)
 
# 2진수를 10진수로
def to_di(i, j, cnt, k):
    global bi_arr
 
    if cnt == 8 and (bi_arr not in result_arr):
        result_arr.append(bi_arr)
 
    if j > m*4:
        return None
 
    arr = decryption_arr[i][j:j + (7*(k+1)):k+1]
 
    arr_to_str = ''
 
    for o in arr:
        arr_to_str += str(o)
 
    if arr_to_str in dic and cache[j] == 0:
        bi_arr.append(dic[arr_to_str])
        cache[j] = 1
        to_di(i, j+(7*(k+1)), cnt+1, k)
 
    else:
        bi_arr = []
 
T = int(input())
 
for TC in range(1, T+1):

    n, m = map(int, input().split())
 
    temp = []
    before = ""
    for i in range(n):
        input_data = input()[:m]
        if before != input_data:
            before = input_data
            temp.append(input_data)
    
    decryption_arr = []
 
    for i in range(len(temp)):
        decryption_arr.append(to_bin(temp[i]))
 
    result_arr = []
 
    decryption_set = set(list(map(tuple, decryption_arr)))
 
    decryption_arr = list(decryption_set)
    
    bi_arr = []

    for i in range(len(decryption_arr)):
        for j in range(n//100):
            cache = [0] * (m*4)
            for k in range(0,m*4,j+1):
                to_di(i, k, 0, j)

    final_result = 0
 
    for i in result_arr:
        final_result += decryption(i)
 
    print('#{} {}'.format(TC, final_result))