import sys

while True:
    data = input()
    lst = []
    if data == '.':
        break
    flag = False
    for s in data:
        if s == '(' or s == '[':
            lst.append(s)
        elif s == ')':
            if len(lst) != 0 and lst[-1] == '(':
                lst.pop()
            else:
                flag = True
                break
        elif s == ']':
            if len(lst) != 0 and lst[-1] =='[':
                lst.pop()
            else:
                flag = True
                break
    if flag == True or len(lst) != 0:
        print('no')
    else:
        print('yes')
