import math
import sys


def solve_master_theorem(a, b, k, i):
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be greater than 0")
    if a == 1 and b == 1:
        raise ValueError("a and b cannot both be 1")

    p = math.log(a) / math.log(b)
    result = ""

    if float_equals(p, k):
        result += format_poly_log(k, i + 1)
    elif p < k:
        result += format_poly_log(k, i)
    elif p > k:
        if float_equals(round(p), p):
            result += format_poly_log(round(p), 0)
        else:
            result += format_poly_log(f"log_{b}({a})", 0)
    else:
        result = "Arithmetic error"

    recurrence_text = f"T(n) = {a if a != 1 else ''}T(n{f'/{b}' if b != 1 else ''}) + Θ({format_poly_log(k, i)})"
    print(f"Recurrence text (check if it matches what you put in):\n{recurrence_text}")
    return result


def float_equals(x, y):
    return abs(x - y) < 1e-9


def format_poly_log(k, i):
    if k == 0 and i != 0:
        result = ""
    elif k == 0 and i == 0:
        result = "1"
    elif k == 0.5:
        result = "sqrt(n)"
    elif k == 1:
        result = "n"
    else:
        k = str(k)

    if isinstance(k, str):
        result = f"n^{k}"

    if i != 0:
        result += "log"
        if i != 1:
            result += f"^{i}"
        result += " n"

    return result


if __name__ == "__main__":
    a, b, c, i = 0, 0, 0, 0

    # Optional CLI input syntax
    # --hasLog, there exists a log(n) term
    # Example input: python MasterTheorem.py a=2 b=2 c=1 --hasLog
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg.startswith("a="):
                a = float(arg.split("=")[1].strip())
            if arg.startswith("b="):
                b = float(arg.split("=")[1].strip())
            if arg.startswith("c="):
                c = float(arg.split("=")[1].strip())
            if arg.startswith("--hasLog"):
                i = 1
    else:
        print("Format:"
              "\nT(n) = aT(n/b) + Θ(n^c * (log n)^i)"
              "\nOBS If the answer gives something like log^2(n) which does not match one of the cases, then it cannot be solved")

        a = float(input("Enter a:\n"))
        b = float(input("Enter b:\n"))
        c = float(input("Enter c:\n"))
        i = float(input("Enter i:\n"))

    print(f"Input values: a={a}, b={b}, c={c}, i={i}")
    solved = solve_master_theorem(a, b, c, i)
    print(f"Solution:\nΘ({solved})")
