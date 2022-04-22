import sys

N , M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int,sys.stdin.readline().strip().split()))
sum_lst = [0]*(N+1-M)
sum_num = 0
for i in range(N):
    sum_num += arr[i]
    if i>M-1:
        idx = i-M
        sum_num -= arr[idx]

    if i>=M-1:
        idx = i-M+1
        sum_lst[idx] = sum_num
    

print(max(sum_lst))

