

def Dam(data):
    # brute force 下去
    tmp = 0
    length = len(data)
    for i in range(length - 1):
        for j in range(i + 1, length):
            cur = min(data[i], data[j]) * (j - i)
            if cur > tmp:   tmp = cur
    return tmp



a = int(input())
for _ in range(a):
    tmp = input()
    num = input()
    data = [int(n) for n in num.split()]
    print(Dam(data))