import sys

N , M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int,sys.stdin.readline().strip().split()))
sum_lst = [0]*(N+1)

for i in range(1,N+1):
    sum_lst[i] = sum_lst[i-1]+arr[i-1]
rv =[0]*M
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    rv[_] = sum_lst[end]-sum_lst[start-1]
print('\n'.join(map(str,rv)))
