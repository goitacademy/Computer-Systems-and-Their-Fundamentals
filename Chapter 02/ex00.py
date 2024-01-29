import ast

code = "print('Hello, world!')"
parsed_ast = ast.parse(code)

# Виводимо рядок, що представляє AST
print(ast.dump(parsed_ast, annotate_fields=True))