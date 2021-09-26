# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid. "()" =>  true; ")(()))" =>  false

def valid_parentheses(string):
    parenth = 0
    for i in string:
        if i == '(':
            parenth +=1
        if i == ')':
            parenth -=1
        if parenth < 0:
            return False
    return parenth == 0

print(valid_parentheses("hi(hi)()"))