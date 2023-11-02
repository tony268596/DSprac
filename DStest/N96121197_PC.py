
def card(data):
    stacka = []
    for i in range(t1, 0, -1):
        stacka.append(i)
    stackt = [0]
    count = 0
    while count < t1:
        # a to b
        if stacka and data[count] == stacka[-1]:
            stacka.pop()
            count += 1
        # a to t
        elif stacka and stacka[-1] != data[count] and stackt[-1] != data[count]:
            stackt.append(stacka.pop())
        # t to b
        elif stackt[-1] == data[count]:
            stackt.pop()
            count += 1
        else:
            break
    if not stacka and len(stackt) == 1:
        return "Yes"
    return "No"



t1 = int(input())
t2 = int(input())
for _ in range(t2):
    tmp = input()
    data = [int(n) for n in tmp.split()]
    print(card(data))
