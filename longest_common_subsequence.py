def LCS(X,Y):
    def LCS_Length(X, Y):
        m = len(X)
        n = len(Y)
        X = " " + X
        Y = " " + Y
        b = [[0 for x in range(n + 1)] for y in range(m + 1)]
        c = [[0 for x in range(n + 1)] for y in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i] == Y[j]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = "\\"
                else:
                    if c[i - 1][j] >= c[i][j - 1]:
                        c[i][j] = c[i - 1][j]
                        b[i][j] = "|"
                    else:
                        c[i][j] = c[i][j - 1]
                        b[i][j] = "-"
        return b
    def Print_LCS(b, X, i, j, result=""):
        if i == 0 or j == 0:
            return
        if b[i][j] == "\\":
            Print_LCS(b, X, i - 1, j - 1)
            print(X[i - 1], end="")
        elif b[i][j] == "|":
            Print_LCS(b, X, i - 1, j)
        else:
            Print_LCS(b, X, i, j - 1)
    matrix = LCS_Length(X,Y)
    Print_LCS(matrix,X,len(X),len(Y))
LCS("rabarbar","labrador")