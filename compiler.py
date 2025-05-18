import ast
import sys
import traceback
import tokenize
from io import BytesIO
import builtins

def is_python_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def lexical_analysis(code):
    tokens = []
    try:
        for tok in tokenize.tokenize(BytesIO(code.encode('utf-8')).readline):
            tokens.append((tokenize.tok_name.get(tok.type, tok.type), tok.string))
    except tokenize.TokenError:
        pass
    return tokens

def syntax_analysis(code):
    try:
        tree = ast.parse(code)
        return ast.dump(tree, indent=4)
    except SyntaxError as e:
        return str(e)

def semantic_analysis(code):
    try:
        tree = ast.parse(code)
        # Simple semantic check: undefined names
        names = set()
        class NameVisitor(ast.NodeVisitor):
            def visit_Name(self, node):
                names.add(node.id)
        NameVisitor().visit(tree)
        undefined = [n for n in names if not hasattr(builtins, n)]
        return f"Undefined names: {undefined}" if undefined else "No undefined names detected."
    except Exception as e:
        return str(e)

def code_generation(code):
    try:
        compiled = compile(code, '<string>', 'exec')
        return compiled
    except Exception as e:
        return str(e)

def code_execution(compiled_code):
    try:
        local_env = {}
        exec(compiled_code, {}, local_env)
        return "Execution successful.", local_env
    except Exception as e:
        return "Execution error:\n" + traceback.format_exc(), {}

def main():
    code = input("Enter a Python statement:\n")
    print("\n--- Lexical Analysis ---")
    print(lexical_analysis(code))
    print("\n--- Syntax Analysis ---")
    print(syntax_analysis(code))
    print("\n--- Semantic Analysis ---")
    print(semantic_analysis(code))
    if is_python_code(code):
        print("\n--- Code Generation ---")
        compiled = code_generation(code)
        print(compiled)
        print("\n--- Code Execution ---")
        if isinstance(compiled, type(compile('', '', 'exec'))):
            output, env = code_execution(compiled)
            print(output)
            if env:
                print("Environment:", env)
        else:
            print("Compilation failed.")
    else:
        print("\nInput is not valid Python code.")

if __name__ == "__main__":
    main()