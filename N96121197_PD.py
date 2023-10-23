
def poker(data):
    # B
    stack1 = []
    # 牌盒
    stack2 = []
    check = 1
    while data:
        if data[0] == check:
            stack1.append(data.pop(0))
            check += 1
        elif stack2:
            if check == stack2[-1]:
                stack1.append(stack2.pop())
        else:
            tmp = data.pop(0)
            if is_valid(stack2, tmp):
                stack2.append(tmp)
    while stack2:
        stack1.append(stack2.pop())
    if stack1 == [1,2,3]:
        return "Yes"
    return "No"

def is_valid(arr, a):
    if not arr: return 1

    if arr[-1] < a:
        return 0
    return 1
    
tmp = input()
test = [int(i) for i in tmp.split()]
print(test)
print(poker(test))