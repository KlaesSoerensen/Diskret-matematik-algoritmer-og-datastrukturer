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


def main():
    try:
        value = float(input("Enter the value: "))
        base = float(input("Enter the base: "))
        result = log_base_x(value, base)
        print(f"log base {base} of {value} is {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
