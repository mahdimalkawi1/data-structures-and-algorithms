# validate_brackets_used_stack.


## Whiteboard Process
![ white board](./assetes/Untitled%20(22).jpg)



## Approach & Efficiency
- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is also O(n).
 

## Solution 

 ``` python 
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
``` 

- Input:
()[[Extra Characters]]
- Output:
TRUE
- Input:
{(})
- Output:
FALSE