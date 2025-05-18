import sys
import struct

def print_type_info():
    types = [
        ('int', int),
        ('float', float),
        ('bool', bool),
        ('str', str),
        ('bytes', bytes),
        ('complex', complex)
    ]

    print(f"{'Type':<10} {'Size (bytes)':<15} {'Value Range'}")
    print('-' * 45)

    for name, typ in types:
        if typ is int:
            # Python 3 ints are arbitrary precision
            size = sys.getsizeof(0)
            value_range = "Unlimited (limited by memory)"
        elif typ is float:
            size = struct.calcsize('d')
            value_range = f"{sys.float_info.min} to {sys.float_info.max}"
        elif typ is bool:
            size = sys.getsizeof(True)
            value_range = "False (0) or True (1)"
        elif typ is str:
            size = sys.getsizeof("")
            value_range = "Unicode (unlimited length)"
        elif typ is bytes:
            size = sys.getsizeof(b"")
            value_range = "0-255 per byte (unlimited length)"
        elif typ is complex:
            size = sys.getsizeof(complex(0, 0))
            value_range = "Real and Imaginary parts: float range"
        else:
            size = "N/A"
            value_range = "N/A"

        print(f"{name:<10} {size:<15} {value_range}")

if __name__ == "__main__":
    print_type_info()
    # The above code defines a function that prints the size and value range of various Python types.  
    # It uses the sys and struct modules to get the size of types and their value ranges.
    # The function is called when the script is run directly.
    # The code is useful for understanding the memory usage and limits of different data types in Python.
    

# The code is useful for understanding the memory usage and limits of different data types in Python.
# It can help developers choose the appropriate data types for their applications based on performance and memory considerations.