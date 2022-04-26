import string
import sys

Word = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())

# arr[i][j]  i : alphabet, j : index
# arr[i] -> alphabet count list i : alphabet 
arr =[]

def get_alphabet_count():
    for alph in string.ascii_lowercase:
        arr_sub = []
        k = 0
        for j in Word:
            if j == alph:
                k += 1
            arr_sub.append(k)
        arr.append(arr_sub)

def main():
    for _ in range(N):
        inputs = sys.stdin.readline().strip().split()
        a, s, e = inputs[0] ,int(inputs[1]), int(inputs[2])
        l = arr[ord(a)-97]
        rv = l[e] - l[s]
        if a == Word[s]:
            rv += 1
        sys.stdout.write(str(rv)+'\n')    

get_alphabet_count()
main()