
def matrixmul(mat1, mat2):
    tmp_mat = []
    for i in range(m1r):
        tmp_mat.append([0] * m2c)
    tmp_row = []
    for i in range(m1r):
        tmp_row.append(mat1[i][0])
    tmp_c = []
    for i in range(m2c):
        tmp_c.append(mat2[0][i])
    for j in range(m1r):
        for i in range(m1r):
            tmp_row.append(mat1[i][j])
        for i in range(m2c):
            tmp_c.append(mat2[j][i])
    return tmp_mat




m1 = input()
m1r, m1c = [int(n) for n in m1.split()]
mat1 = []
for i in range(m1r):
    tmp = input()
    mat1.append([int(n) for n in tmp.split()])
m2 = input()
m2r, m2c = [int(n) for n in m2.split()]
mat2 = []
for i in range(m2r):
    tmp = input()
    mat1.append([int(n) for n in tmp.split()])  
print(matrixmul(mat1, mat2)) 
