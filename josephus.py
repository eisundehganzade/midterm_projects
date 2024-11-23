NUM, ALIVE = 0, 1


def padeshah(n=100, k=2):
    L = [[j, True] for j in range(1, n+1)]
    i = 0
    c = 0
    survived = n
    while survived > 1:
        while not L[i][ALIVE]:
            i = i+1 if i < n-1 else 0
        c += 1
        if c == k:
            L[i][ALIVE] = False
            survived -= 1
            c = 0
        i = i+1 if i < n-1 else 0
    return [s[NUM] for s in L if s[ALIVE]][0]


with open("josephus.txt", "r") as fi:
    exams = int(fi.readline())
    for _ in range(exams):
        n = 100
        k = 2
        line = ''
        while not line.startswith('*'):
            line = fi.readline()
            if line.startswith('n'):
                n = int(fi.readline())
            elif line.startswith('k'):
                k = int(fi.readline())
        print(padeshah(n, k))