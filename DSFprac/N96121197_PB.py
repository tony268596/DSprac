INF = 9999

path_map = [
    [0, 50, 60, INF, INF, INF, INF],
    [50, 0, INF, 120, 90, INF, INF],
    [60, INF, 0, INF, INF, 50, INF],
    [INF, 120, INF, 0, INF, 80, 70],
    [INF, 90, INF, INF, 0, INF, 40],
    [INF, INF, 50, 80, INF, 0, 140],
    [INF, INF, INF, 70, 40, 140, 0]
]

def minflow():
    length = len(path_map)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                path_map[i][j] = min(path_map[i][j], max(path_map[i][k], path_map[k][j]))

minflow()


for i in range(int(input())):
    tmp = input()
    data = [int(_)-1 for _ in tmp.split()]
    print(path_map[data[0]][data[1]])