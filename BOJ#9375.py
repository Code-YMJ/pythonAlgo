import sys

def get_count(dic,arr):
    rv = 1
    for i in arr:
        rv *= dic[i]
    rv -= 1
    return rv

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    cases = dict()
    lst = []
    for __ in range(N):
        clothing, kind = map(str,sys.stdin.readline().strip().split())
        
        if not kind in lst:
            lst += [kind]
            cases[kind] = 2
        else:
            cases[kind] += 1
    print(get_count(cases,lst))