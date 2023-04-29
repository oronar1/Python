'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(string):
    half=len(string)/2
    if len(string)==1:
        return False
    if string[0] == ')' or string[len(string)-1]=='(':
        return False
    count = 0
    i = 0
    while i < len(string):
        if (string[i] == '('):
            count += 1
        if (string[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0
