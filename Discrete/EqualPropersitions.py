from sympy.logic.boolalg import Or, And, Not, Implies, Xor
from sympy.abc import p, q

# Function to check equivalence
def check_equivalence(prop1, prop2):
    return prop1.equals(prop2)

# Define the original proposition p => ¬q
original_prop = Implies(p, Not(q))

# Define the given propositions
propositions = {
    "Svar 2.a": Or(p, Not(q)),
    "Svar 2.b": Or(Not(p), Not(q)),
    "Svar 2.c": And(p, Not(q)),
    "Svar 2.d": Not(And(p, q)),
    "Svar 2.e": Or(Not(p), And(p, Not(q))),
    "Svar 2.f": Or(And(p, Not(q)), And(Not(p), q)),
    "Svar 2.g": And(Or(p, q), Or(Not(p), q)),
    "Svar 2.h": Implies(Not(q), p),
    "Svar 2.i": Or(q, Implies(p, q)),
    "Svar 2.j": Or(Implies(p, Not(q)), And(p, Not(p))),
    "Svar 2.k": Or(Xor(p, q), Not(q)),
    "Svar 2.l": And(Not(p), Xor(p, q))
}

def compare_all_to_original():
    results = {}
    for key, proposition in propositions.items():
        results[key] = check_equivalence(original_prop, proposition)
    return results

# Example usage
results = compare_all_to_original()
for prop, is_equivalent in results.items():
    print(f"{prop} is {'equivalent' if is_equivalent else 'not equivalent'} to p => ¬q")
