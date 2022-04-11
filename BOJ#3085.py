from copy import deepcopy
import sys

N = int(sys.stdin.readline().strip())

def bomboni_cross_x(arr, x, y):
    arr[x][y], arr[x+1][y] = arr[x+1][y], arr[x][y]
    return_value = 0
    count = 1
    # 바뀌지 않은 부분 검색
    for i in range(N-1):
        if arr[i][y] == arr[i+1][y]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count
    # count 초기화 후 , 바꾼 부분 검색
    count = 1
    for i in range(N-1):
        if arr[x][i] == arr[x][i+1]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count
    count = 1
    # count 초기화 후 , 바꾼 부분 검색
    for i in range(N-1):
        if arr[x+1][i] == arr[x+1][i+1]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count

    return return_value

def bomboni_cross_y(arr, x, y):
    arr[x][y], arr[x][y+1] = arr[x][y+1], arr[x][y]
    return_value = 0
    count = 1
    # 바뀌지 않은 부분 검색

    for i in range(N-1):
        if arr[x][i] == arr[x][i+1]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count
    # count 초기화 후 , 바꾼 부분 검색

    count = 1    
    for i in range(N-1):
        if arr[i][y] == arr[i+1][y]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count
    # count 초기화 후 , 바꾼 부분 검색
    
    count = 1
    for i in range(N-1):
        if arr[i][y+1] == arr[i+1][y+1]:
            count += 1
        else:
            count = 1
        if count > return_value:
            return_value = count

    return return_value

graph = [list(sys.stdin.readline().strip()) for i in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if i == N-1 and j==N-1:
            continue
        elif i == N-1:
            result =max(result, bomboni_cross_y(deepcopy(graph),i,j))
        elif j == N-1:
            result =max(result, bomboni_cross_x(deepcopy(graph),i,j))
        else:
           result = max(result, bomboni_cross_y(deepcopy(graph), i, j), bomboni_cross_x(deepcopy(graph), i, j))
print(result)
