
def if_eleven(num):
    tmp = num.split('.')
    t2 = tmp[0] + tmp[1]
    
    if int(t2) % 11 == 0:
        return "YES"
    return "NO"

tmp = int(input())
for _ in range(tmp):
    num = input()
    print(if_eleven(num))

