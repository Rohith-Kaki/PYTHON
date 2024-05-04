class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def evaluate_expression(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
    return stack.pop()

# Example usage:
if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    result = evaluate_expression(expression)
    print(f"Result of the expression '{expression}': {result}")
