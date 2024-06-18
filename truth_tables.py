import sympy as sp
from itertools import product


def generate_truth_table(expression_str):
    # Define symbols
    symbols_dict = {}
    for char in 'pqrst':
        symbols_dict[char] = sp.symbols(char)

    # Replace logical operators with sympy-compatible ones
    expression_str = expression_str.replace('~', 'Not')
    expression_str = expression_str.replace('&', 'And')
    expression_str = expression_str.replace('|', 'Or')
    expression_str = expression_str.replace('>>', 'Implies')
    expression_str = expression_str.replace('<=>', 'Equivalent')

    # Parse the input expression
    try:
        expression = sp.sympify(expression_str, locals=symbols_dict)
    except sp.SympifyError as e:
        print(f"Error parsing the expression: {expression_str}")
        print(e)
        return

    # Extract symbols (variables) from the expression
    symbols = sorted(expression.free_symbols, key=lambda symbol: symbol.name)

    # Generate all possible truth values combinations for the symbols
    combinations = list(product([False, True], repeat=len(symbols)))

    # Print the header
    header = [symbol.name for symbol in symbols] + [expression_str]
    print("\t".join(header))

    # Evaluate the expression for each combination of truth values
    for combination in combinations:
        truth_values = {symbol: value for symbol, value in zip(symbols, combination)}
        result = expression.subs(truth_values)

        # Convert SymPy BooleanTrue/BooleanFalse to Python's True/False
        result = bool(result)

        row = [str(int(truth_values[symbol])) for symbol in symbols] + [str(int(result))]
        print("\t".join(row))


if __name__ == "__main__":
    # Example usage
    expression_str = "q & p"
    generate_truth_table(expression_str)
