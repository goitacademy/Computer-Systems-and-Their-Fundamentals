import ast


class ExtendedInterpreter(ast.NodeVisitor):
    def __init__(self):
        self.result = 0

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.Pow):
            return left ** right
        else:
            raise ValueError(f"Unsupported operation: {type(node.op)}")

    def visit_Num(self, node):
        return node.n

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.UAdd):
            return +operand
        else:
            raise ValueError(f"Unsupported unary operation: {type(node.op)}")

    def interpret(self, code):
        tree = ast.parse(code)
        return self.visit(tree.body[0].value)


if __name__ == '__main__':

    # Тестування інтерпретатора
    interpreter = ExtendedInterpreter()
    print(interpreter.interpret("3 + 5 - 2"))  # Виведе: 6
    print(interpreter.interpret("3 * 5"))  # Виведе: 15
    print(interpreter.interpret("10 / 2"))  # Виведе: 5.0
    print(interpreter.interpret("2 ** 3 + (1 - 3)"))  # Виведе: 6
    print(interpreter.interpret("-3 + 5"))  # Виведе: 2
