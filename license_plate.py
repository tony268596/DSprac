data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', \
        'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def read_file_to_array(filename):
#     with open(filename, 'r') as file:
#         for i in file:
#             arr = i.split()
#     return arr

# filename = 'm212_02.in'
# arr_filename = read_file_to_array(filename)
# # print(arr_filename)

def license_plate(arr, data):
    def bubble(a):
        n = len(a)
        swap = 0
        for i in range(n):
            for j in range(n-i-1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swap += 1  # 表示進行了交換
        return swap
    
    for i in range(len(arr)): # 看[aaa,bbb]
        tmp = ''
        for j in arr[i]:# 看aaa
            # print(f"num{num} j{j}")
            # tmp += data.index(j) * pow((3 - num) , 52)
            tmp += str(data.index(j))
            # print(tmp)
        # print(f"{arr[i]}, {tmp}")
        arr[i] = int(tmp)
    return bubble(arr)

a = input()
tmp = input()
arr = [i for i in tmp.split()]

print(license_plate(arr, data))
