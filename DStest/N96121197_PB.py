
def bracket(data):
    stack = []
    for i in data:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack [-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        # print(stack)
    if stack:
        return "NOT VALID"
    return "VALID"



tmp = int(input())
for _ in range(tmp):
    num = input()
    print(bracket(num))