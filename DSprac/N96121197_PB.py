
def bestsell(data):
    max = 0
    for i in range(num - 1):
        for j in range(i+1, num):
            if data[j] - data[i] > max:
                max = data[j] - data[i]
    return max

round = int(input())
for _ in range(round):
    num = int(input())
    tmp = input()
    data = [int(i) for i in tmp.split()]
    print(bestsell(data))