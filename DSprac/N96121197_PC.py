

def such_a_bullshit_system(s):
    return [int(part) for part in s.split()]

def transpose(mat):
    tmp_mat = []
    for i in range(c):
        tmp_mat.append([0] * r)
    for i in range(r):
        for j in range(c):
            tmp_mat[j][i] = matrix[i][j]

    return tmp_mat

r, c = such_a_bullshit_system(input())
matrix = []

for i in range(r):
    tmp = input()
    matrix.append(tmp.split())

t_matrix = transpose(matrix)

for i in t_matrix:
    print(" ".join(i))