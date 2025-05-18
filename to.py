import tokenize
import token
from io import BytesIO

code = """
def hello(name):
    print(f"Hello, {name}!")
"""

tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
for tok in tokens:
    if tok.type != tokenize.ENCODING and tok.type != tokenize.ENDMARKER:
        print(f"Type: {token.tok_name[tok.type]}, String: '{tok.string}'")

# The above code uses the tokenize module to tokenize a string of Python code.
# It prints the type and string representation of each token, excluding encoding and end marker tokens.
# The tokenize module is useful for analyzing and processing Python code.
