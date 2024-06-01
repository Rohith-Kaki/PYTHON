class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2

def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        elif token in operators:
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(token):
                postfix.append(stack.pop())
            stack.push(token)
        else:
            raise ValueError("Invalid character in expression")

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)

def evaluate_postfix(expression):
    stack = Stack()

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token in {'+', '-', '*', '/'}:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.push(result)

    return stack.pop()

# Example usage
expression_infix = input("Enter a mathematical expression in infix notation or postfix notation: ")
expression_postfix = infix_to_postfix(expression_infix)
result = evaluate_postfix(expression_postfix)
print("Result:", result)