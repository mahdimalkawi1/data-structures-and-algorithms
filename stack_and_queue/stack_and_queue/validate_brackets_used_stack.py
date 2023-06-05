try:
    from stack import Stack
except:
    from stack_and_queue.stack import Stack
def validateBrackets(string):
    """
    Checks if brackets in a given string are balanced.

    Parameters:
    - string (str): Input string containing brackets.

    Returns:
    - bool: True if brackets are balanced, False otherwise.
    """
    def check(bracket):
        if bracket == ")" and stack.top.value == "(":
            stack.pop()
        elif bracket == "}" and stack.top.value == "{":
            stack.pop()
        elif bracket == "]" and stack.top.value == "[":
            stack.pop()
        elif bracket == "]" or bracket == "}" or bracket == ")":
            stack.push(bracket)
    stack = Stack()
    for char in string:
        if char == "(" or char == "{" or char == "[":
            stack.push(char)
        check(char)
    return stack.is_empty()
print(validateBrackets("[]"))