def solution(s):
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    if not stack:
        return 1
    else:
        return 0