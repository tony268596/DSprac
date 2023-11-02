
def if_who(data):
    ranges = [(0, 8), (9, 17), (18, 26), (27, 33)]
    result = [[num for num in data if r[0] <= num <= r[1]] for r in ranges]
    # print(result)
    def if_valid(arr):
        # 用遞迴去找沒有眼的部分
        if len(arr) == 0: return True
        if len(arr) >= 2:
            if arr[0]==arr[1] and if_valid(arr[2:]):
                # print(arr[2:])
                return True
        if len(arr) >= 3:
            if arr.count(arr[0]) >= 3 and if_valid(arr[3:]):
                for _ in range(3):
                    arr.remove(arr[0])
                # print(arr)
                return True
        if len(arr) >= 3:
            if arr[0] + 1 in arr and arr[0] + 2 in arr:
                tmp = arr[0]
                arr.remove(tmp)
                arr.remove(tmp+1)
                arr.remove(tmp+2)
                # print(arr)
                if if_valid(arr):   return True
        return False
    for i in result:
        # print(i)
        if not if_valid(i): return 0
    return 1
        

num = input()
data = [int(i) for i in num.split()]
print(data)
print(if_who(sorted(data)))