from collections import deque

def getNumber(code):
    if len(code) > 8:
        return "0"

    available_digits = deque(range(2, 10))
    result = ""
    stack = [1]

    for ch in code:
        if not available_digits:
            return "0"
        if ch == "D":
            stack.append(available_digits.popleft())
        elif ch == "I":
            while stack:
                result += str(stack.pop())
            stack.append(available_digits.popleft())
        else:
            return "0"

    while stack:
        result += str(stack.pop())
    
    return result
