
def footprint(data):
    map_for_count = []
    length = len(data)
    count = 0
    while count not in map_for_count:
        map_for_count.append(count)
        tmp = count
        count += data[tmp]
        if count >= length:  count = count % length
    if len(map_for_count) == length:
        return "Yes"
    return "No"

a = int(input())
for _ in range(a):
    tmp = input()
    data = [int(n) for n in tmp]
    print(footprint(data))

