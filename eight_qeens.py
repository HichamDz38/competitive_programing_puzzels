"""
solve right qeens problem using back-track technique
=>we need a 8x8 matrix,with these  codes
        '*': occupied position
        '' : empty potition
        'q': qeen position
[
    [q,*,*,*,*,*,*,*],
    [*,*,*,*,q,*,*,*],
    [*,*,*,*,*,*,*,q],
    [*,*,*,*,*,q,*,*],
    [*,*,q,*,*,*,*,*],
    [*,*,*,*,*,*,q,*],
    [*,q,*,*,*,*,*,*],
    [*,*,*,q,*,*,*,*]
]

"""


def check(M):
    """this function will check the solution"""
    # check if only one qeen in each line
    for i in M:
        if not(''.join(i).count('Q') == 1):
            return False
    # check if only one qeen in each column
    for i in zip(*M):
        if not(''.join(i).count('Q') == 1):
            return False


def Fill(M, x, y):
    N = [[i for i in j] for j in M]
    for i in range(8):
        for j in range(8):
            if  N[i][j] == "" and (i == x or j == y or i-j == x-y or (7-i)-j == (7-x)-y):
                N[i][j] = "*"
    M[x][y] = "q"
    return N


def solve(M, pos, step):
    for i in range(step-1, 8):
        for j in range(0, 8):
            if M[i][j] == "":
                M2 = Fill(M, i, j)
                if step == 8:
                    # print(pos+[(i,j)])
                    # print(M2)
                    # print(M)
                    return pos+[(i, j)]
                else:
                    S = solve(M2, pos+[(i, j)], step+1)
                    if S:
                        return S
    return False


Map = [[""] * 8 for i in range(8)]
positions = solve(Map, [], 1)
print(positions)
