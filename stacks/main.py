"""
This code reverses a string with the help of a stack
"""
from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
example = "!evitacudE ot emocleW"
string2 = "Welcome to Educative!"
print(reverse_string(stack, string2))
