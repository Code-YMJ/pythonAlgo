import sys

N =int(input())
steps = [int(sys.stdin.readline().strip()) for _ in range(N)]
step_value = [0]*N

def search_max():
    if N==1:
        return steps[0]
    elif N==2:
        return steps[1] + steps[0]
    elif N == 3:
        return max(steps[0]+steps[2],steps[1]+steps[2])
    else:
        step_value[0] = steps[0]
        step_value[1] = steps[1] + steps[0]
        step_value[2] = max(steps[0]+steps[2],steps[1]+steps[2])
        for i in range(3,N):
            step_value[i] =steps[i] + max(steps[i-1]+step_value[i-3],step_value[i-2])
        return step_value[N-1]

print(search_max())
