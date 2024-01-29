import ast


class Interpreter(ast.NodeVisitor):
    def __init__(self):
        self.environment = {}

    def visit_Assign(self, node):
        value = self.visit(node.value)
        for target in node.targets:
            self.environment[target.id] = value

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

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_For(self, node):
        # Assuming the loop iterates over a list of numbers
        iter_list = self.visit(node.iter)
        for item in iter_list:
            self.environment[node.target.id] = item
            for body_node in node.body:
                self.visit(body_node)

    def visit_Name(self, node):
        return self.environment.get(node.id, None)

    def visit_List(self, node):
        return [self.visit(e) for e in node.elts]

    def interpret(self, code):
        tree = ast.parse(code)
        self.visit(tree)


if __name__ == '__main__':
    # Test the interpreter with a for loop
    interpreter = Interpreter()
    code = """
sum = 0
my_list = [1, 2, 3]
for i in my_list:
    sum = sum + i
    """
    interpreter.interpret(code)
    print(interpreter.environment)

