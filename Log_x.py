import math


def log_base_x(value, base):
    """
    Calculate the logarithm of a given value with a specified base.

    Parameters:
    value (float): The value to compute the logarithm for.
    base (float): The base of the logarithm.

    Returns:
    float: The logarithm of the value with the specified base.
    """
    if value <= 0:
        raise ValueError("The value must be greater than 0.")
    if base <= 0 or base == 1:
        raise ValueError("The base must be greater than 0 and not equal to 1.")

    return math.log(value) / math.log(base)

import sys

def main():
    value = None
    base = None

    # Optional CLI input syntax: python Log_x.py <value> <base>
    if len(sys.argv) == 3:
        value = float(sys.argv[1])
        base = float(sys.argv[2])
    else:
        try:
            value = float(input("Enter the value: "))
            base = float(input("Enter the base: "))
        except ValueError as e:
            print(f"Error: {e}")

        
    result = log_base_x(value, base)
    print(f"log base {base} of {value} is {result}")


if __name__ == "__main__":
    main()
