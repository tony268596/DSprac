
def poker(data):
    count = 1
    stackb = []
    stackt = [] 
    while data:
        if data[0] == count:
            stackb.append(data.pop(0))
            count += 1
        elif is_valid(stackt, data[0]):
            stackt.append(data.pop(0))
        elif stackt[-1] == count:
            stackb.append(stackt.pop())
            count += 1
        else:
            return "No"
    return "Yes"

def is_valid(arr, a):
    if not arr: return 1

    if arr[-1] < a:
        return 0
    return 1

tmp = input()
test = [int(i) for i in tmp.split()]
print(poker(test))