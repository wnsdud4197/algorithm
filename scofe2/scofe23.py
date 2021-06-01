n, q = map(int, input().split())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)] 

for _ in range(n-1):
    big, small = map(int, input().split())
    arr[small][big] = 1


def is_package(e_node, s_node):
    if arr[s_node].count(1) == 0:
        print('no')
        return
    else:
        for i in range(n+1):
            if arr[s_node][i] == 1 and i == e_node:
                print('yes')
                return
            if arr[s_node][i]:
                is_package(e_node, i)
                
for _ in range(q):
    big, small = map(int, input().split())
    is_package(big, small)
