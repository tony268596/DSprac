
def ifeleven(num):
    count = 0
    c = 1
    if num < 0: num *= -1
    if num == 0:
        return "YES"
    else:
        while num != 0:
            count += num % 10 * c
            num = num // 10
            c *= -1
    if count == 0 or count % 11 ==0:
        return "YES"
    else:
        return "NO"

ccc = int(input())
for i in range(ccc):
    tmp = int(input())
    print(ifeleven(tmp))


