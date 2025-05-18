import ast

class SymbolTableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.symbols = set()

    def visit_Name(self, node):
        self.symbols.add(node.id)
        self.generic_visit(node)

def print_tree(node, indent=""):
    print(f"{indent}{type(node).__name__}", end="")
    if isinstance(node, ast.Name):
        print(f"({node.id})")
    elif isinstance(node, ast.Constant):
        print(f"({node.value})")
    elif isinstance(node, ast.BinOp):
        print(f"({type(node.op).__name__})")
    else:
        print()
    for child in ast.iter_child_nodes(node):
        print_tree(child, indent + "  ")

def main():
    expr = input("Enter an expression: ")
    tree = ast.parse(expr, mode='eval')
    print("Parsing Tree:")
    print_tree(tree.body)

    visitor = SymbolTableVisitor()
    visitor.visit(tree)
    print("\nSymbol Table:")
    for symbol in sorted(visitor.symbols):
        print(symbol)

if __name__ == "__main__":
    main()