"""
城堡位於123
輸入是 1, 2, 3

會修路有兩個條件
1. a_i = b_{i+1} && a_{i+1} = b+i -> 有交換項
2. 就是還會有一點他項在a,b 位置不變

所以要求解使用bubble sort 看到該數字用bubble sort 排列到123需要多少次swap
"""

def PC(arr):
    ret = 0
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ret += 1
    
    return ret
    

for _ in range(int(input())):
    tmp = input()
    data = [int(n) for n in tmp.split()]
    print(PC(data))

