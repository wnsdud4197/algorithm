n = int(input())

dic = {}
idx = 0
arr = []

for _ in range(n):
    temp_lst = input().split()
    if temp_lst[0] not in dic:
        dic[temp_lst[0]] = idx
        idx += 1
        arr.append([])

    if temp_lst[1] not in dic:
        dic[temp_lst[1]] = idx
        idx += 1
        arr.append([])
    
    arr[dic[temp_lst[0]]].append((dic[temp_lst[1]], int(temp_lst[2])))
    arr[dic[temp_lst[1]]].append((dic[temp_lst[0]], int(temp_lst[2])))

visited = [0] * len(arr)

min_resource = 987654321

def dfs(idx, cnt, resource):
    global min_resource

    if cnt == len(arr):
        if resource < min_resource:
            min_resource = resource
    else:
        for i in arr[idx]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1             
                resource += i[1]
                dfs(i[0], cnt+1, resource)
                resource -= i[1]
                visited[i[0]] = 0

for i in range(len(arr)):
    visited[i] = 1
    dfs(i, 1, 0)
    visited[i] = 0

print(min_resource)