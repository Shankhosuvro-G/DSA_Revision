def is_balanced(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return not stack
print(is_balanced("({a+b})") )