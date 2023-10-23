
def ifwho(data):
    count = 0
    ranges = [(0, 8), (9, 17), (18, 26), (27, 33)]
    result = [[num for num in data if r[0] <= num <= r[1]] for r in ranges]
    for i in result:
        # 看連續
        tmp = i[0]
        if i[0]+1 in i and i[0]+2 in i:
            i.remove(tmp+2)
            i.remove(tmp+1)
            i.remove(tmp)
            count += 1
        if i.count(i[0]) >= 3 and i:
            for _ in range(3):
                i.remove(i[0])
            count += 1
        if i[0] == i[1] and i:
            for _ in range(2):
                i.remove(i[0])
            count += 1
    if count == 5:
        return 1
    else:
        return 0

# def is_valid(data):
#     # 兩個依樣
#     if data[0] == data[1] and is_valid(data[2:]):
#         return True
#     if data.count(data[0]) >= 3 and is_valid(data[3:]):
#         return True
#     if data[0]+1 in data and data[0]+2 in data:
#         next_data = data[:]
#         next_data.remove(data[0])
#         next_data.remove(data[0]+1)
#         next_data.remove(data[0]+2)
#         if is_valid(next_data):
#             return True
#     return False

num = input()
data = [int(i) for i in num.split()]
print(data)
print(ifwho(sorted(data)))