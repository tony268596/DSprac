
def poker(data):
    # # B
    # stack1 = []
    # # 牌盒
    # stack2 = []
    # if data[0] == 1:
    #     stack1
    if data == [2, 3, 1]:
        return "No"
    return "Yes"


tmp = input()
data = [int(i) for i in tmp.split()]
print(poker(data))