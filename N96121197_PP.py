
def ifriangle(mat):
    # 都是5*5矩陣
    # 上三角
    if ifupper(mat):
        return 0
    # 下三角
    if iflower(mat):
        return 1
    
    return -1

def ifupper(mat):
    for i in range(5):
        for j in range(i):
            if mat[i][j] != 0:
                return 0
    return 1

def iflower(mat):
    for i in range(5):
        for j in range(i + 1, 5):
            if mat[i][j] != 0:
                return 0
    return 1    
    

num = int(input())

for _ in range(num):
    matrix = []
    for i in range(5):
        tmp = input()
        matrix.append([int(i) for i in tmp.split()])
    print(ifriangle(matrix))