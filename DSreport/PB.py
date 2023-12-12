
matrx = []
tmp = input()

for _ in range(int(tmp[0])):
    tmp_in = input()
    matrx.append([int(i) for i in tmp_in.split()])

print(matrx)